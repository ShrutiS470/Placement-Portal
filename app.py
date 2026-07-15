from flask import Flask, config, render_template, request, redirect, url_for, jsonify, make_response

from models import db, user_datastore, company, student, drive, application, placement
from flask_security import Security, auth_required, roles_required, roles_accepted #pip install flask-security-too
from datetime import datetime


def create_app():
    init_app = Flask(__name__)
    from config import localdev
    init_app.config.from_object(localdev)

    security = Security(init_app, user_datastore)
    db.init_app(init_app)

    from flask_restful import Api
    init_api = Api(init_app)
    from flask_cors import CORS
    CORS(init_app)

    from mailer import mailer
    mailer.init_app(init_app)

    from caching import cache
    cache.init_app(init_app)

    
    from celery import Celery
    init_celery = Celery(init_app.import_name)
    import celery_config
    init_celery.config_from_object(celery_config)
    
    
    return init_app, init_api, init_celery
    #return init_app, init_api

app , api, app_celery = create_app()
#app, api = create_app()

from celery import Celery
app_celery = Celery(app.import_name)
import celery_config
app_celery.config_from_object(celery_config)
#from config import celeryConfig
#app_celery.config_from_object(celeryConfig)
import celerytask

from celery.schedules import crontab
app_celery.conf.beat_schedule = {
    "daily_shortlisted_reminder": {
        "task": "celerytask.daily_shortlisted_reminder",
        "schedule": crontab(minute=0, hour=8)
    },
    "monthly-report": {
        "task": "tasks.monthly_activity_report",
        "schedule": crontab(
            day_of_month=1,
            hour=8,
            minute=0
        ),
    },
}


@app.route('/export-applications', methods=['POST'])
@auth_required('token')
@roles_required('student')
def post():
    data = request.json
    student_id = data.get('student_id')
    task = celerytask.export_application_csv.delay(student_id)
    while not task.ready():
        pass
    return jsonify({
            "message": "CSV export started",
            "task_id": task.id
        })

@app.route('/', methods=['POSt'])
@auth_required('token')#decorator to require authentication for this route, using token-based authentication
@roles_required('student')#specifies that the user must have the 'student' role to access this route
def home():
    return {"message": "Welcome to the Placement Portal API!"}

from routes.auth import signup, signin
api.add_resource(signup, '/signup')
api.add_resource(signin, '/signin')

from routes.registration import company_registration, student_registration
api.add_resource(company_registration, '/com_register')
api.add_resource(student_registration, '/stud_register')

from routes.admin import AdminDashboard
api.add_resource(AdminDashboard, '/admin')

from routes.drive import Drive, CreateDrive
api.add_resource(Drive, '/drive/<int:id>')
api.add_resource(CreateDrive, '/create_drive')

from routes.application import Application, CreateApplication
api.add_resource(Application, '/application/<int:id>')
api.add_resource(CreateApplication, '/create_application')

from routes.Company import Company, DriveApplications
api.add_resource(DriveApplications, '/drive_applications/<int:id>')
api.add_resource(Company, '/company/<int:id>')

from routes.Student import StudentDashboard, StudentApplications, StudentDrive
api.add_resource(StudentDashboard, '/student_dashboard/<int:id>')
api.add_resource(StudentApplications, '/student_applications/<int:id>')
api.add_resource(StudentDrive, '/student_drive/<int:id>')


if __name__ == '__main__':
    app.run()