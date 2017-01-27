import datetime

from flask_security import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from App import db
from . import hash_512


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(200), index=True)
    email = db.Column(db.VARCHAR(200), nullable=True)
    appid = db.Column(db.VARCHAR(512), nullable=True)
    name = db.VARCHAR(db.VARCHAR(200))
    password =db.Column("pass", db.VARCHAR(512), nullable=True)
    active = db.Column("status", db.SmallInteger, default=0) # 0 -> user not verified, 1 -> user verified
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    roles = db.Column(db.Integer, default=0)

    links = db.relationship('ConfirmationLink',
                    backref=db.backref('user', lazy='joined'), lazy='dynamic')

    @hybrid_property
    def roles(self):
        return []

    @roles.setter
    def roles(self, role):
        pass

    @classmethod
    def create_user(cls, username='', email='', password=''):
        return User(username=username, email=email, password=password)

    def generate_api_key(self):
        self.appid = hash_512(datetime.datetime.now())

    def set_password(self, password_str):
        self.password = hash_512(password_str)

    def check_password(self, password):
        return self.password == hash_512(password)