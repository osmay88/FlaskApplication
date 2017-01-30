from flask import make_response
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from App import _db, User


class LoginUser(Resource):
    def __init__(self, *args, **kwargs):
        self.reqparse = reqparse.RequestParser()

        if request.json:
            self.reqparse.add_argument('username', type=str, required=True,
                                       help='Username field is required',
                                       location=['json', 'headers', 'values'])
            self.reqparse.add_argument('password', type=str, required=True,
                                       help='The password is required',
                                       location=['json', 'headers', 'values'])
        else:
            self.reqparse.add_argument('username', type=str, required=True,
                                       help='Username field is required')
            self.reqparse.add_argument('password', type=str, required=True,
                                       help='The password is required')

        super(LoginUser, self).__init__(*args, **kwargs)

    def post(self):
        values = self.reqparse.parse_args()
        user = _db.session.query(User).filter_by(username=values.get("username")).first()

        if not user.active:
            return make_response(jsonify({"error": "The user is not active."}), 401)

        if user is not None and user.check_password(values.get("password")):
            ret = {
                'access_token': create_access_token(user.__as_dict__())
            }
            return make_response(jsonify(ret), 200)
        return make_response(jsonify({"error": "Bad username or password"}), 401)
