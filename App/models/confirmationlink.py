import datetime

from App import db
from App.models.user import User

from . import hash_md5


class ConfirmationLink(db.Model):
    __tablename__ = "confirmationlink"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.Text(512))
    active = db.Column(db.SmallInteger, default=1)  # 0 -> link have been visited, 1 -> waiting for customer
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    expire_on = db.Column(db.Date, default=datetime.date.today() + datetime.timedelta(10))

    @classmethod
    def create_link(cls):
        return cls(link=hash_md5(datetime.datetime.now()))

    def activate(self):
        self.active = 0
