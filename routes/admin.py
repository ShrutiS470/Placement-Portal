from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, user_datastore, company, student, application, drive
from flask_security import Security, auth_required, roles_required, roles_accepted

class AdminDashboard(Resource):
    @auth_required('token')
    #@roles_required('student')
    #@cache.cached()
    def get(self):
        # Get all companies
        companies = company.query.all()
        company_list = []
        for comp in companies:
            company_list.append({
                'id': comp.com_id,
                'name': comp.com_name,
                'status': comp.user.active
            })
        
        # Get all students
        students = student.query.all()
        student_list = []
        for stud in students:
            student_list.append({
                'id': stud.stu_id,
                'name': stud.name,
                })
        drives = drive.query.all()
        drive_list = []
        for dr in drives:
            drive_list.append({
                'id': dr.drive_id,
                'job': dr.job_title,
                'company': dr.company.com_name
            })
    
        applications = application.query.all()
        application_list = []
        for app in applications:
            application_list.append({
                'id': app.app_id,
                'student': app.student.name,
                'drive': app.drive.job_title,
                'company': app.drive.company.com_name,
            })   
        
        return jsonify({
            'companies': company_list,
            'students': student_list,
            'drives': drive_list,
            'applications': application_list
        })