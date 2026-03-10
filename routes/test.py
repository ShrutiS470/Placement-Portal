from flask_restful import Resource
from flask import request, jsonify, make_response

class Testapi(Resource):
    def get(self):
        return make_response(jsonify({"status": "success"}), 200)
    
    def post(self):
        data= request.get_json()
        return make_response(jsonify({"message": "post working"}), 201)
    
    def put(self):
        data= request.get_json()
        return data, 200
    def delete(self):
        return make_response(jsonify({"message": "success"}), 200)