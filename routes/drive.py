from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, user_datastore, company, student, application, drive
from flask_security import Security, auth_required, roles_required, roles_accepted
from caching import cache

class Drive(Resource):
    @auth_required('token')
    @roles_accepted('student','admin')
    @cache.cached()
    def get(self, id):
        dr = drive.query.filter_by(drive_id=id).first()
        if not dr:
            return make_response(jsonify({'message': 'Drive not found'}), 404)
        drive_data = {
            'id': dr.drive_id,
            'job_title': dr.job_title,
            'description': dr.job_description,
            'application_deadline': dr.application_deadline,
            'company': dr.company.com_name
        }
        return make_response(jsonify(drive_data), 200)