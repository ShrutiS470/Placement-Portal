from models import db, user_datastore, student, company, drive, application, placement
from app import create_app
from datetime import datetime

app, _ = create_app()

with app.app_context():
    db.create_all()
    user_datastore.find_or_create_role(name='admin')
    user_datastore.find_or_create_role(name='company')
    user_datastore.find_or_create_role(name='student')
    db.session.commit()

    if not user_datastore.find_user(email='a@abc.com'):
        admin_user = user_datastore.create_user(email='a@abc.com', password='a')
        role = user_datastore.find_role('admin')
        user_datastore.add_role_to_user(admin_user, role)
        db.session.commit()

    if not user_datastore.find_user(email='company@xyz.com'):
        company_user = user_datastore.create_user(email='company@xyz.com', password='company')
        role = user_datastore.find_role('company')
        user_datastore.add_role_to_user(company_user, role)
        print("Company user created")

    if not user_datastore.find_user(email='student@abc.com'):
        student_user = user_datastore.create_user(email='student@abc.com', password='student')
        role = user_datastore.find_role('student')
        user_datastore.add_role_to_user(student_user, role)
        print("Student user created")

    db.session.commit()

    admin_user = user_datastore.find_user(email='a@abc.com')
    company_user = user_datastore.find_user(email='company@xyz.com')
    student_user = user_datastore.find_user(email='student@abc.com')

    company1 = company(user_id=company_user.id, com_name='TechCorp', website='https://www.techcorp.com', industry='Software', location='San Francisco')
    student1 = student(user_id=student_user.id, name='Jai ram', phone='1234567890', degree='B.Tech', branch='Computer Science', year_of_passing=2026)
    db.session.add(company1)
    db.session.add(student1)
    db.session.commit()
    print("Company and Student records created")

    drive1 = drive(com_id=company1.com_id, job_title='Software Engineer', job_description='Develop and maintain software applications.', eligibility_criteria='B.Tech in Computer Science', application_deadline=datetime(2026, 3, 15), approval_status='approved')
    drive2 = drive(com_id=company1.com_id, job_title='Data Analyst', job_description='Analyze data and generate insights.', eligibility_criteria='B.Tech in Computer Science or related field', application_deadline=datetime(2026, 3, 14), approval_status='approved')
    drive3 = drive(com_id=company1.com_id, job_title='Product Manager', job_description='Oversee product development and strategy.', eligibility_criteria='B.Tech in Computer Science or related field', application_deadline=datetime(2026, 3, 15), approval_status='approved')
    drive4 = drive(com_id=company1.com_id, job_title='UX Designer', job_description='Design user interfaces and experiences.', eligibility_criteria='B.Tech in Computer Science or related field', application_deadline=datetime(2026, 3, 16), approval_status='approved')
    db.session.add(drive1)
    db.session.add(drive2)
    db.session.add(drive3)
    db.session.add(drive4)
    db.session.commit()
    print("Drive records created")

    application1 = application(stu_id=student1.stu_id, drive_id=drive1.drive_id, status='applied', date=datetime(2026, 2, 20))
    application2 = application(stu_id=student1.stu_id, drive_id=drive2.drive_id, status='applied', date=datetime(2026, 2, 21))
    application3 = application(stu_id=student1.stu_id, drive_id=drive3.drive_id, status='applied', date=datetime(2026, 2, 22))
    application4 = application(stu_id=student1.stu_id, drive_id=drive4.drive_id, status='applied', date=datetime(2026, 2, 23))
    db.session.add(application1)
    db.session.add(application2)
    db.session.add(application3)
    db.session.add(application4)
    db.session.commit()
    print("Application records created")

    placement1 = placement(stu_id=student1.stu_id, com_id=company1.com_id, job_title='Software Engineer', salary=10.0, date_of_joining=datetime(2026, 4, 1))
    db.session.add(placement1)
    db.session.commit()
    print("Placement record created")

    print("Database initialization complete.")