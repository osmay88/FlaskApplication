import datetime

from App import _db
from . import hash_md5, hash_512


class User(_db.Model):
    __tablename__ = "user"
    id = _db.Column(_db.Integer, primary_key=True, autoincrement=True)
    username = _db.Column(_db.VARCHAR(200), index=True)
    email = _db.Column(_db.VARCHAR(200), nullable=True)
    appid = _db.Column(_db.VARCHAR(200), nullable=True)
    name = _db.VARCHAR(_db.VARCHAR(200))
    password = _db.Column("pass", _db.VARCHAR(512), nullable=True)
    active = _db.Column(_db.SmallInteger, default=0)  # 0 -> user not verified, 1 -> user verified

    links = _db.relationship('ConfirmationLink',
                             backref=_db.backref('user', lazy='joined'), lazy='dynamic')

    @classmethod
    def create_user(cls, username='', email='', password=''):
        return User(username=username, email=email, password=password)

    def generate_api_key(self):
        self.appid = hash_md5(datetime.datetime.now())

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

    def __as_dict__(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
