from flask import current_app, jsonify
from flask import make_response
from flask_jwt_extended import get_jwt_claims
from flask_jwt_extended import jwt_required
from flask_mail import Message
from flask_restful import Resource

from App import _db, User, mail


class GenerateApiKey(Resource):
    @jwt_required
    def post(self):
        claims = get_jwt_claims()
        user = _db.session.query(User).filter_by(id=claims["id"]).first()

        if user is None:
            return make_response(jsonify({"error": "Invalid user id"}), 400)

        if user.appid is not None:
            return make_response(jsonify({"error": "The user already have a app-id"}), 400)

        if not user.active:
            return make_response(jsonify({"error": "The user is not activated"}), 400)

        user.generate_api_key()
        _db.session.commit()

        msg = Message("Hello",
                      sender=current_app.config["MAIL_USERNAME"],
                      recipients=[user.email, ])
        msg.html = current_app.config["API_KEY_TEMPLATE"].format(user.appid)
        mail.send(msg)
        return make_response(jsonify({"appid": user.appid}), 200)
