from flask import make_response
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from App import db, User


class LoginUser(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        if request.json:
            self.reqparse.add_argument('username', type=str, required=True,
                                       help='Username field is required',
                                       location=['json', 'headers', 'values'])
            self.reqparse.add_argument('password', type=str, required=True,
                                       help='The password is required',
                                       location=['json', 'headers', 'values'])

    def post(self):
        values = self.reqparse.parse_args()
        user = db.session.query(User).filter_by(username=values.get("username")).first()
        if user.check_password(values.get("password")):
            ret = {'access_token': create_access_token(values.get("username"))}
            return make_response(jsonify(ret), 200)
        return jsonify({"msg": "Bad username or password"}), 401