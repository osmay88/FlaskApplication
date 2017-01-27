import datetime

from App import db
from . import hash_512


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(200), index=True)
    email = db.Column(db.VARCHAR(200), nullable=True)
    appid = db.Column(db.VARCHAR(512), nullable=True)
    name = db.VARCHAR(db.VARCHAR(200))
    password = db.Column("pass", db.VARCHAR(512), nullable=True)
    active = db.Column(db.SmallInteger, default=0)  # 0 -> user not verified, 1 -> user verified

    links = db.relationship('ConfirmationLink',
                            backref=db.backref('user', lazy='joined'), lazy='dynamic')

    @classmethod
    def create_user(cls, username='', email='', password=''):
        return User(username=username, email=email, password=password)

    def generate_api_key(self):
        self.appid = hash_512(datetime.datetime.now())

    def set_password(self, password_str):
        self.password = hash_512(password_str)

    def check_password(self, password):
        return self.password == hash_512(password)

    def update_password(self, old_password, new_password):
        if self.password != hash_512(old_password):
            return False
        self.password = hash_512(new_password)
        return True

    def activate(self):
        self.active = 1
