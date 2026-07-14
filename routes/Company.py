from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, user_datastore, company, student, application, drive
from flask_security import Security, auth_required, roles_required, roles_accepted
from caching import cache

class Company(Resource):
    @auth_required('token')
    @roles_accepted('company','admin')
    @cache.cached()
    def get(self, id):
        comp = company.query.filter_by(user_id=id).first()
        if not comp:
            return make_response(jsonify({'message': 'Company not found'}), 404)
        company_data = {
            'id': comp.com_id,
            'name': comp.com_name,
            'email': comp.user.email,
            'status': comp.user.active
        }
        drives = drive.query.filter_by(com_id=comp.com_id).all()
        drive_list = []
        for dr in drives:
            drive_list.append({
                'id': dr.drive_id,
                'job': dr.job_title,
                'company': dr.company.com_name
            })
        company_data['drives'] = drive_list
        return make_response(jsonify(company_data), 200)

class DriveApplications(Resource):
    @auth_required('token')
    @roles_accepted('company','admin')
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
        applications = application.query.filter_by(drive_id=dr.drive_id).all()
        application_list = []
        for app in applications:
            application_list.append({
                'id': app.app_id,
                'student': app.student.name,
                'department': app.student.branch,
                'status': app.status
            })
        drive_data['applications'] = application_list
        return make_response(jsonify(drive_data), 200)     