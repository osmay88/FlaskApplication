from flask import make_response
from flask import request, jsonify
from flask_restful import Resource, reqparse

from App import db, User


class UpdateUser(Resource):
    def __init__(self, *args, **kwargs):
        self.reqparse = reqparse.RequestParser()

        if request.json:
            self.reqparse.add_argument('oldpassword', type=str, required=True,
                                       help='Username field is required',
                                       location=['json', 'headers', 'values'])
            self.reqparse.add_argument('newpassword', type=str, required=True,
                                       help='The password is required',
                                       location=['json', 'headers', 'values'])
        else:
            self.reqparse.add_argument('oldpassword', type=str, required=True,
                                       help='Username field is required')
            self.reqparse.add_argument('newpassword', type=str, required=True,
                                       help='The password is required')

        super(UpdateUser, self).__init__(*args, **kwargs)

    def post(self, userid):
        values = self.reqparse.parse_args()
        user = db.session.query(User).filter_by(id=userid).first()

        if user is not None:
            if user.update_password(old_password=values["oldpassword"], new_password=values["newpassword"]):
                return make_response(jsonify("Password updated"), 200)
            else:
                return make_response(jsonify({"error": "Old password and new password doesnt match"}), 400)
        else:
            return make_response(jsonify({"error": "Invalid user id"}), 400)
