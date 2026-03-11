from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import MutableList
from flask_security import UserMixin, RoleMixin, AsaList, SQLAlchemyUserDatastore

db = SQLAlchemy()

class RolesUsers(db.Model):
    __tablename__ = "roles_users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

class Role(db.Model, RoleMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True) # needed
    name = db.Column(db.String(50), unique=True, nullable=False) #needed
    #description = db.Column(db.String(255)) #optional
    #permissions = db.Column(MutableList.as_mutable(AsaList()), nullable=True) #optional

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) #needed
    email = db.Column(db.String(120), unique=True, nullable=False) #needed
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False) #needed
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean()) #needed
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) #needed
    #confirmed_at = db.Column(db.DateTime())
    roles = db.relationship("Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic"))
    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

class company(db.Model):
    com_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    com_name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    user = db.relationship("User", backref="companies")

class student(db.Model):
    stu_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    year_of_passing = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", backref="students")

class drive(db.Model):
    drive_id = db.Column(db.Integer, primary_key=True)
    com_id = db.Column(db.Integer, db.ForeignKey('company.com_id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    eligibility_criteria = db.Column(db.Text, nullable=False)
    application_deadline = db.Column(db.DateTime, nullable=False)
    approval_status = db.Column(db.String(20), nullable=False)  # 'pending', 'approved', 'rejected'
    company = db.relationship("company", backref="drives")
    
class application(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('student.stu_id'), nullable=False)
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.drive_id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'applied', 'shortlisted', 'rejected'
    date = db.Column(db.DateTime, nullable=False)
    student = db.relationship("student", backref="applications")
    drive = db.relationship("drive", backref="applications")

class placement(db.Model):
    place_id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('student.stu_id'), nullable=False)
    com_id = db.Column(db.Integer, db.ForeignKey('company.com_id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(100), nullable=False)
    date_of_joining = db.Column(db.DateTime, nullable=False)
    student = db.relationship("student", backref="placements")
    company = db.relationship("company", backref="placements")
