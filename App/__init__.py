# from celery import Celery
from flask import Flask
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
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




