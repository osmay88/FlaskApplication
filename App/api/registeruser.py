from flask import make_response
from flask import request, current_app
from flask.json import jsonify
from flask_mail import Message
from flask_restful import Resource, reqparse, marshal_with
from flask_restful import fields

from App import mail, db
from App.models import User, ConfirmationLink

from . import UserDto

resource_fields = {
    'id': fields.String,
    'username': fields.String,
    'email': fields.String,
    'status': fields.Boolean,
    'error': fields.String
}


class RegisterUser(Resource):
    def __init__(self, *args, **kwargs):
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
        else:
            self.reqparse.add_argument('username', type=str, required=True,
                                       help='Username field is required')
            self.reqparse.add_argument('email', type=str, required=True,
                                       help='Email address is required')
            self.reqparse.add_argument('password', type=str, required=True,
                                       help='The password is required')
        super(RegisterUser, self).__init__(*args, **kwargs)

    @marshal_with(resource_fields)
    def post(self):
        args = self.reqparse.parse_args()
        if User.query.filter_by(username=args.get("username")).first():
            return UserDto(error="That username already exists"), 400

        if User.query.filter_by(email=args.get("email")).first():
            return UserDto(error="That email already exists"), 400

        new_user = User.create_user(args["username"], args["email"])
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
        dto = UserDto(username=str(new_user.username), email=str(new_user.email), id=new_user.id, status=new_user.active)
        return dto, 201
