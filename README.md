# Placement-Potal
Portal to cordinate between companies, students and institutes.


To start the project -

1. Frontend- Open the terminal in Frontend protal and follow the instruction available in the readme there.

2. Backend- Open another terminal in the 'Placement-Portal' folder and start a venv using below command.
        python -m venv .venv   //for first time set up.
        . .venv/bin/activate
        pip install -r requirement.txt    //for first time set up.
        python app.py

3. Redis - Open another terminal in the 'Placement-Portal' folder and start the redis server using-
        redis-server
    To stop the redis server-
        sudo service redis-server stop

4. Celery Worker - Open another terminal with venv as per above instruction. Ensure that Backend is already running.
        celery -A app.app_celery worker --loglevel=INFO

5. Celery beat - Open another terminal with venv as per above instruction. Ensure that Backend is already running.
        celery -A app.app_celery beat --loglevel=INFO

6. Mailpit - mailpit
