import datetime

from App import _db
from App.models.user import User

from . import hash_md5


class ConfirmationLink(_db.Model):
    __tablename__ = "confirmationlink"
    id = _db.Column(_db.Integer, primary_key=True, autoincrement=True)
    link = _db.Column(_db.Text(512))
    active = _db.Column(_db.SmallInteger, default=1)  # 0 -> link have been visited, 1 -> waiting for customer
    user_id = _db.Column(_db.Integer, _db.ForeignKey(User.id), nullable=False)
    expire_on = _db.Column(_db.Date, default=datetime.date.today() + datetime.timedelta(10))

    @classmethod
    def create_link(cls):
        return cls(link=hash_md5(datetime.datetime.now()))

    def activate(self):
        self.active = 0
