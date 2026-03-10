from flask import Flask, config, render_template, request, redirect, url_for

from models import db, user_datastore, company, student, drive, application, placement
from flask_security import Security, auth_required, roles_required, roles_accepted #pip install flask-security-too
from datetime import datetime

def create_app():
    init_app = Flask(__name__)
    from config import localdev
    init_app.config.from_object(localdev)

    security = Security(init_app, user_datastore)
    db.init_app(init_app)

    from flask_restful import Api
    init_api = Api(init_app)
    from flask_cors import CORS
    CORS(init_app)
    
    return init_app, init_api

app, api = create_app()


@app.route('/', methods=['POSt'])
@auth_required('token')#decorator to require authentication for this route, using token-based authentication
@roles_required('student')#specifies that the user must have the 'student' role to access this route
def home():
    return {"message": "Welcome to the Placement Portal API!"}

from routes.auth import signup, signin
api.add_resource(signup, '/signup')
api.add_resource(signin, '/signin')

if __name__ == '__main__':
    app.run()