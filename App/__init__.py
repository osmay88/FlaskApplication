import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

config_settings = os.environ.get('ENV_SETTINGS')

if config_settings is None:
    app.config.from_object('config.Development')
else:
    app.config.from_object(config_settings)

db = SQLAlchemy(app)

jwt = JWTManager(app)


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'id': identity["id"],
        'username': identity["username"]
    }

_api = Api(app)

from .models import *

mail = Mail(app)

from .api import *

_api.add_resource(RegisterUser, '/register')
_api.add_resource(ConfirmUser, '/confirm/<string:userlink>')
_api.add_resource(LoginUser, '/loginuser')
_api.add_resource(UpdateUser, '/update')
_api.add_resource(GenerateApiKey, '/generatekey')
