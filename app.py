from flask import Flask, config, render_template, request, redirect, url_for

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

    '''
    from celery import Celery
    init_celery = Celery(init_app.import_name)
    import celery_config
    init_celery.config_from_object(celery_config)
    '''
    
    #return init_app, init_api, init_celery
    return init_app, init_api

#app, api, app_celery = create_app()
app, api = create_app()

from celery import Celery
app_celery = Celery(app.import_name)
import celery_config
app_celery.config_from_object(celery_config)
#from config import celeryConfig
#app_celery.config_from_object(celeryConfig)
import celerytask

from celery.schedules import crontab
app_celery.conf.beat_schedule = {
    "schedule1": {
        "task": "celerytask.add",
        "schedule": crontab(minute=7, hour=15),
        "args": (16, 16)
    }
}

#from celery import Task
'''
@app_celery.task()
def add(a,b):
    return a+b

@app_celery.task()
def hello():
    print("Hello world")
    return "Hello"
'''

@app.route('/testcelery', methods=['POST'])
def testcelery():
    data = request.json
    a,b = data.get('a'), data.get('b')
    result = celerytask.hello.delay()
    celerytask.test_email.delay()
    #result = celerytask.add.delay(a,b)
    while not result.ready():
        pass
    return {"status":result.status, "id":result.id}, 201

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

from routes.drive import Drive
api.add_resource(Drive, '/drive/<int:id>')

if __name__ == '__main__':
    app.run()