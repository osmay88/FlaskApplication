from flask import current_app
from flask_mail import Message
from flask_restful import Resource

from App import db, User, mail


class GenerateApiKey(Resource):

    def post(self, userid):
        user = db.session.query(User).filter_by(id=userid).first()

        if user is None:
            return {"error":"Invalid user id"}, 400

        if user.appid is not None:
            return {"error":"The user aready have a appid"}, 400

        if not user.active:
            return {"error":"The user is not activated"}, 400

        user.generate_api_key()
        db.session.commit()



        msg = Message("Hello",
                      sender="osmay.cruz@gmail.com",
                      recipients=["osmay.cruz@gmail.com"])
        msg.html = current_app.config["API_KEY_TEMPLATE"].format(user.appid)
        mail.send(msg)
        #send_async_email.delay(msg)
        return {"appid": user.appid}, 200