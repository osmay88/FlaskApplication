# from celery import Celery
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

jwt = JWTManager(app)

# Using the user_claims_loader, we can specify a method that will be
# called when creating access tokens, and add these claims to the said
# token. This method is passed the identity of who the token is being
# created for, and must return data that is json serializable
# @jwt.user_claims_loader
# def add_claims_to_access_token(identity):
#     return {
#         'hello': identity,
#         'foo': ['bar', 'baz']
#     }

_api = Api(app)

from .models import *

mail = Mail(app)

# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)
#
# @celery.task
# def send_async_email(msg):
#     """Background task to send an email with Flask-Mail."""
#     with app.app_context():
#         mail.send(msg)



from .api import *

_api.add_resource(RegisterUser, '/register')
_api.add_resource(ConfirmUser, '/confirm/<string:userlink>')
_api.add_resource(LoginUser, '/loginuser')
_api.add_resource(GenerateApiKey, '/<int:userid>/generatekey')




