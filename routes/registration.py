from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, company, student

class company_registration(Resource):
    def post(self):
        data = request.json
        user_id = data.get("user_id")
        com_name = data.get("com_name")
        website = data.get("website")
        industry = data.get("industry")
        location = data.get("location")
        if not all([user_id, com_name, website, industry, location]):
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        if company.query.filter_by(user_id=user_id).first():
            return make_response(jsonify({"error": "details already updated"}), 400)
        new_company = company(user_id=user_id, com_name=com_name, website=website, industry=industry, location=location)
        db.session.add(new_company)
        db.session.commit()
        return make_response(jsonify({"status": "Company registration successful"}), 200)

class student_registration(Resource):
    def post(self):
        data = request.json
        user_id = data.get("user_id")
        name = data.get("name")
        phone = data.get("phone")
        degree = data.get("degree")
        branch = data.get("branch")
        year_of_passing = data.get("year_of_passing")
        if not all([user_id, name, phone, degree, branch, year_of_passing]):
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        new_student = student(user_id=user_id, name=name, phone=phone, degree=degree, branch=branch, year_of_passing=year_of_passing)
        db.session.add(new_student)
        db.session.commit()
        return make_response(jsonify({"status": "Student registration successful"}), 200)