from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placements.sqlite3'

db = SQLAlchemy(app)

class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student', 'admin', 'company'

class company(db.Model):
    com_id = db.Column(db.Integer, primary_key=True)
    com_name = db.Column(db.String(100), nullable=False)
    HR_contact = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    approval_status = db.Column(db.String(20), nullable=False)  # 'pending', 'approved', 'rejected'

class student(db.Model):
    stu_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    year_of_passing = db.Column(db.Integer, nullable=False)

class drive(db.Model):
    drive_id = db.Column(db.Integer, primary_key=True)
    com_id = db.Column(db.Integer, db.ForeignKey('company.com_id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    eligibility_criteria = db.Column(db.Text, nullable=False)
    application_deadline = db.Column(db.DateTime, nullable=False)
    approval_status = db.Column(db.String(20), nullable=False)  # 'pending', 'approved', 'rejected'
    
class application(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('student.stu_id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'applied', 'shortlisted', 'rejected'
    date = db.Column(db.DateTime, nullable=False)

class placement(db.Model):
    place_id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('student.stu_id'), nullable=False)
    com_id = db.Column(db.Integer, db.ForeignKey('company.com_id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(100), nullable=False)
    date_of_joining = db.Column(db.DateTime, nullable=False)

with app.app_context():
    db.create_all()

    admin_exists = user.query.filter_by(username='admin').first()
    if not admin_exists:
        admin_password = generate_password_hash('admin123')
        admin = user(username='admin', email='admin@clg.in', password=admin_password, role='admin')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)