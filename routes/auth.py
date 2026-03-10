from flask import request, jsonify, make_response
from flask_restful import Resource
from models import db, user_datastore

#@app.route('/signup', methods=['POST'])
class signup(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        if not email:
            return {"status": "Email is required"}, 400
        password = data.get('password')
        if not password:
            return {"status": "Password is required"}, 400
        role = data.get('role')
        if not role:
            return {"status": "role is required"}, 400
        if "admin" in role:
            return {"status": "Cannot create admin user"}, 400
        #from models import user
        #new_user = user(email=email, password=password)
        #db.session.add(new_user)
        if user_datastore.find_user(email=email):
            return {"status": "User already exists"}, 400
        #user_datastore.create_user(email=email, password=password, roles=[role])
        user = user_datastore.create_user(email=email, password=password)
        if "company" in role:
            user_datastore.deactivate_user(user)
        for role in role:
            user_datastore.add_role_to_user(user, role)
        db.session.commit()

        return make_response(jsonify({"status": "success", "id": user.id}), 200)

#@app.route('/signin', methods=['POST'])
class signin(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        if not email:
            return {"status": "Email is required"}, 400
        password = data.get('password')
        if not password:
            return {"status": "Password is required"}, 400
        
        user = user_datastore.find_user(email=email)
        if  user and user.password == password:
            token = user.get_auth_token()
            return make_response(jsonify({"status": "signin successful", "auth_token": token, "roles": user.roles[0].name}), 200)
