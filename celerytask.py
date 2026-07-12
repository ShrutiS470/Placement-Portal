from celery import Task
from app import app_celery, create_app
app_instance, _ =create_app()

class appContext(Task):
    def __call__(self, *args, **kwargs):
        with app_instance.app_context():
            return self.run(*args, **kwargs)


@app_celery.task(base=appContext)
def add(a,b):
    import time
    time.sleep(5)
    return a+b

@app_celery.task(base=appContext)
def hello():
    print("Hello world")
    return "Hello"

@app_celery.task(base=appContext)
def search_student(a):
    from models import student
    stu = student.query.filter_by(id=a).first()
    if stu:
        print("name:", stu.name, "phone:", stu.phone)
        return stu.id
    else:
        return "not found"

@app_celery.task(base=appContext)
def test_email():
    from models import User
    all_user = User.query.all()
    for user in all_user:
        if not user.roles[0].name == "admin":
            print(user.email)
            from flask_mail import Message
            email_receiver = user.email
            email_subject = "Test Email"
            email_body = "We are trying to send and email"
            var1 = Message()
            var1.subject = email_subject
            var1.recipients = [email_receiver]
            var1.body = email_body
            from mailer import mailer
            mailer.send(var1)
    return "Emails sent"