import os


# In this file you setup the application configuration
# you can check here http://flask.pocoo.org/docs/0.12/config/
# The configuration class used is set inside App/__init__.py
# Line app.config.from_object('config.DevelopmentConfig')
class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'aaaaaaa2222222kkkkkkkkk5kkkkdddd000000'
    JWT_SECRET_KEY = 'aaacbafr2222222kkkkkkkkk5kkrrdddd0033400'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_DEBUG=DEBUG
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER=''
    MAIL_MAX_EMAILS=''
    MAIL_SUPPRESS_SEND=''
    MAIL_ASCII_ATTACHMENTS=False

    # Celery configuration
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    REGISTER_TEMPLATE = """
    <H1>Super cool email</H1>
    <p>Here i send you a super cool email about your registration
    To activate your account please click this link<a href="http://127.0.0.1:5000/confirm/{0}">ACTIVATE</a>
    <p>
    """

    API_KEY_TEMPLATE = """
    <H1>Super cool email</H1>
    <p>Here i send you a super cool email about your registration
    Now you have activated your account and we send you your api key
     KEY: {0}
    <p>
    """


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://your_user@your_server/your_database"