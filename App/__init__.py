from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

jwt = JWTManager(app)

_api = Api(app)

from .models import *

mail = Mail(app)

from .api import *

_api.add_resource(RegisterUser, '/register')
_api.add_resource(ConfirmUser, '/confirm/<string:userlink>')
_api.add_resource(LoginUser, '/loginuser')
_api.add_resource(UpdateUser, '/<int:userid>/update')
_api.add_resource(GenerateApiKey, '/<int:userid>/generatekey')
