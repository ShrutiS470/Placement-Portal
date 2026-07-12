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