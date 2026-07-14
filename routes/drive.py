from datetime import datetime
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

class CreateDrive(Resource):
    @auth_required('token')
    @roles_required('company')
    def post(self):
        data = request.get_json()
        com_id = data.get('com_id')
        job_title = data.get('job_title')
        job_description = data.get('job_description')
        eligibility_criteria = data.get('eligibility_criteria')
        application_deadline = data.get('application_deadline')
        application_deadline = datetime(*map(int, application_deadline.split('-'))) if application_deadline else None

        if not all([com_id, job_title, job_description, eligibility_criteria, application_deadline]):
            return make_response(jsonify({'message': 'Missing required fields'}), 400)
        new_drive = drive(com_id=com_id, job_title=job_title, job_description=job_description, eligibility_criteria=eligibility_criteria, application_deadline=application_deadline, approval_status='approved')
        db.session.add(new_drive)
        db.session.commit()
        return make_response(jsonify({'message': 'Drive created successfully', 'drive_id': new_drive.drive_id}), 201)