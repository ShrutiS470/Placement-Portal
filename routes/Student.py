from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, user_datastore, company, student, application, drive
from flask_security import Security, auth_required, roles_required, roles_accepted
from caching import cache

class StudentDashboard(Resource):
    @auth_required('token')
    @roles_required('student')
    @cache.cached()
    def get(self, id):
        stud = student.query.filter_by(user_id=id).first()
        if not stud:
            return make_response(jsonify({'message': 'Student not found'}), 404)
        student_data = {
            'id': stud.stu_id,
            'name': stud.name,
            'email': stud.user.email,
            'department': stud.branch
        }
        companies = company.query.filter(company.user.has(active=True)).all()
        company_list = []
        for comp in companies:
            company_list.append({
                'id': comp.com_id,
                'name': comp.com_name
            })
        student_data['companies'] = company_list
        return make_response(jsonify(student_data), 200)
    
class StudentApplications(Resource):
    @auth_required('token')
    @roles_required('student')
    @cache.cached()
    def get(self, id):
        stud = student.query.filter_by(user_id=id).first()
        if not stud:
            return make_response(jsonify({'message': 'Student not found'}), 404)
        student_data = {
            'id': stud.stu_id,
            'name': stud.name,
            'email': stud.user.email,
            'department': stud.branch
        }
        applications = application.query.filter_by(stu_id=stud.stu_id).all()
        application_list = []
        for app in applications:
            application_list.append({
                'id': app.app_id,
                'drive': app.drive.job_title,
                'company': app.drive.company.com_name,
                'status': app.status
            })
        student_data['applications'] = application_list
        return make_response(jsonify(student_data), 200)