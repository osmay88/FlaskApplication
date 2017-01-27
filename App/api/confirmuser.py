from flask import make_response, jsonify
from flask_restful import Resource

from App import db, ConfirmationLink


class ConfirmUser(Resource):

    def get(self, userlink):
        link = db.session.query(ConfirmationLink).filter_by(link=userlink, active=1).first()

        if link is None:
            return make_response(jsonify({"error": "The confirmation links doesnt exists or have been used already."}), 400)

        link.activate()
        link.user.activate()
        db.session.commit()
        return make_response(jsonify("Your account have been activated"), 200)
