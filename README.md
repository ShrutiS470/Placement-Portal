# Placement-Potal
Portal to cordinate between companies, students and institutes.


## Description

This project is a Placement Portal designed to streamline communication and coordination between companies, students, and institutes during the campus recruitment process. It provides a centralized platform where students can create and manage their profiles, apply for internships and job opportunities, track their application status, and receive placement-related updates. Companies can post open roles, review candidate profiles, shortlist applicants, and communicate with recruitment teams efficiently. Institutes can manage placement records, monitor student participation, and coordinate recruitment drives more effectively.

The platform aims to reduce manual effort, improve transparency, and make the recruitment process more organized and accessible for all stakeholders. It supports a structured workflow for job postings, candidate applications, and communication, helping students discover opportunities while enabling companies and institutions to manage hiring in a smoother, data-driven manner.

Key features of the system include:

- Student registration and profile management
- Job posting and recruiter management for companies
- Application tracking and status updates for students
- Institute-level monitoring and coordination of placement activity
- Automated notifications and email-based communication
- Asynchronous task processing using Redis and Celery
- Scalable backend architecture to support placement workflows

Overall, this portal acts as a bridge between academia and industry, making the placement process more efficient, transparent, and collaborative for everyone involved.

## Project Setup

1. Frontend- Open the terminal in Frontend folder and follow the instruction available in the readme there.

2. Backend- Open another terminal in the 'Placement-Portal' folder and start a venv using below command.
 ```bash
python -m venv .venv   #for first time set up.
. .venv/bin/activate
pip install -r requirement.txt    #for first time set up.
python init_db.py       #for first time set up.
```
The seeded SQLite database is created at instance/placements.sqlite3 and is intentionally excluded from Git. The database structure is as follows-

![alt text](<Placement-Portal (1).png>)

```bash
python app.py
```

3. Redis - Open another terminal in the 'Placement-Portal' folder and start the redis server using-
```bash
redis-server
```
To stop the redis server-
```bash
sudo service redis-server stop
```

4. Celery Worker - Open another terminal with venv as per above instruction. Ensure that Backend is already running.
```bash
celery -A app.app_celery worker --loglevel=INFO
```

5. Celery beat - Open another terminal with venv as per above instruction. Ensure that Backend is already running.
```bash
celery -A app.app_celery beat --loglevel=INFO
```

6. Mailpit
```bash
mailpit
```
