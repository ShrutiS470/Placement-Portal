import os
import csv
from celery import Task
from app import app_celery, create_app
app_instance, _ ,_=create_app()

class appContext(Task):
    def __call__(self, *args, **kwargs):
        with app_instance.app_context():
            return self.run(*args, **kwargs)

from models import db, user_datastore, application, drive

@app_celery.task(base=appContext)
def monthly_activity_report():
    total_drives = drive.query.count()
    total_applications = application.query.count()

    selected_students = application.query.filter_by(
        status="Selected"
    ).count()

    html = f"""
    <h1>Monthly Placement Activity Report</h1>

    <p>Total Drives Conducted: {total_drives}</p>
    <p>Total Applications: {total_applications}</p>
    <p>Total Students Selected: {selected_students}</p>
    """

    message = Message(
        subject="Monthly Placement Activity Report",
        recipients=["a@abc.com"],
        html=html
    )

    mailer.send(message)

    return "Monthly report sent"

@app_celery.task(base=appContext)
def daily_shortlisted_reminder():
    shortlisted_applications = application.query.filter_by(status='shortlisted').all()
    for app in shortlisted_applications:
        student_email = app.student.user.email
        drive_title = app.drive.job_title
        company_name = app.drive.company.com_name
        mailer.send_email(
            subject='Shortlisted for Drive',
            recipients=[student_email],
            body=f'Congratulations! You have been shortlisted for the drive "{drive_title}" by "{company_name}". Please check your application status for further details.'
        )
        return f"{len(shortlisted_applications)} reminder emails sent"
    
@app_celery.task(base=appContext)
def export_application_csv(student_id):

    from models import application
    applications = application.query.filter_by(
        stu_id=student_id
    ).all()

    filename = f"applications_{student_id}.csv"

    filepath = os.path.join(
        "static",
        "exports",
        filename
    )

    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )

    with open(filepath, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "Company Name",
            "Drive Title",
            "Application Status",
            "Application Date"
        ])

        for application in applications:

            writer.writerow([
                student_id,
                application.drive.company.com_name,
                application.drive.job_title,
                application.status,
                application.date
            ])

    return filename