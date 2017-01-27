from flask import request, current_app
from flask_mail import Message
from flask_restful import Resource, reqparse, marshal_with

from App import mail, db
from App.models import User, ConfirmationLink

from . import UserDto

from flask_restful import fields

resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'status': fields.Boolean
}


class RegisterUser(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        if request.json:
            self.reqparse.add_argument('username', type=str, required=True,
                                       help='Username field is required',
                                       location=['json', 'headers', 'values'])
            self.reqparse.add_argument('email', type=str, required=True,
                                       help='Email address is required',
                                       location=['json', 'headers', 'values'])
            self.reqparse.add_argument('password', type=str, required=True,
                                       help='The password is required',
                                       location=['json', 'headers', 'values'])
    @marshal_with(resource_fields)
    def post(self):
        args = self.reqparse.parse_args()
        if User.query.filter_by(username=args.get("username")).first():
            return "That user already exists"

        new_user = User.create_user(args["username"],args["email"])
        new_user.set_password(args["password"])
        link = ConfirmationLink.create_link()
        new_user.links.append(link)

        db.session.add(new_user)
        db.session.commit()

        msg = Message("Hello",
                      sender="osmay.cruz@gmail.com",
                      recipients=["osmay.cruz@gmail.com"])
        msg.html = current_app.config["REGISTER_TEMPLATE"].format(link.link)
        mail.send(msg)
        #send_async_email.delay(msg)
        return UserDto(username=str(new_user.username), email=str(new_user.email), id=new_user.id, status=new_user.active), 200