import os
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


_config = os.environ.get('ENV_SETTINGS')


def init_app(_config=None):
    app = Flask(__name__)

    if _config is None:
        app.config.from_object('config.Development')
    else:
        app.config.from_object(_config)
    return app


def init_db(app=None):
    return SQLAlchemy(app)

_app = init_app(_config)

_db = init_db(_app)

jwt = JWTManager(_app)

mail = Mail(_app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'id': identity["id"],
        'username': identity["username"]
    }

_api = Api(_app)

from .models import *
from .api import *
#from .client import client_bp

#_app.register_blueprint(client_bp)

_api.add_resource(RegisterUser, '/register', endpoint="register")
_api.add_resource(ConfirmUser, '/confirm/<string:userlink>', endpoint="confirm")
_api.add_resource(LoginUser, '/loginuser', endpoint="login")
_api.add_resource(UpdateUser, '/update', endpoint="update")
_api.add_resource(GenerateApiKey, '/generatekey', endpoint="generatekey")