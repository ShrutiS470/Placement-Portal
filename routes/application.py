from datetime import datetime
from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, user_datastore, company, student, application, drive
from flask_security import Security, auth_required, roles_required, roles_accepted
from caching import cache

class Application(Resource):
    @auth_required('token')
    @roles_accepted('company','admin')
    @cache.cached()
    def get(self, id):
        app = application.query.filter_by(app_id=id).first()
        if not app:
            return make_response(jsonify({'message': 'Application not found'}), 404)
        application_data = {
            'id': app.app_id,
            'student': app.student.name,
            'department': app.student.branch,
            'drive': app.drive.job_title,
            'company': app.drive.company.com_name,
            'status': app.status
        }
        return make_response(jsonify(application_data), 200)
    
    @auth_required('token')
    @roles_accepted('company')
    def put(self, id):
        app = application.query.filter_by(app_id=id).first()
        if not app:
            return make_response(jsonify({'message': 'Application not found'}), 404)
        data = request.get_json()
        status = data.get('status')
        if status not in ['Applied', 'Shortlisted', 'Rejected', 'Selected']:
            return make_response(jsonify({'message': 'Invalid status value'}), 400)
        app.status = status
        db.session.commit()
        return make_response(jsonify({'message': 'Application status updated successfully'}), 200)
    
class CreateApplication(Resource):
    @auth_required('token')
    @roles_required('student')
    def post(self):
        data = request.get_json()
        stu_id = data.get('stu_id')
        drive_id = data.get('drive_id')
        date = datetime.today()
        if not all([stu_id, drive_id]):
            return make_response(jsonify({'message': 'Missing required fields'}), 400)
        new_application = application(stu_id=stu_id, drive_id=drive_id, status='Applied', date=date)
        db.session.add(new_application)
        db.session.commit()
        return make_response(jsonify({'message': 'Application created successfully', 'app_id': new_application.app_id}), 201)