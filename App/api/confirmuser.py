from flask_restful import Resource

from App import db, ConfirmationLink


class ConfirmUser(Resource):

    def get(self, userlink):
        l = db.session.query(ConfirmationLink).filter_by(link=userlink, active=1).first()
        if l == None:
            return "The confirmation links doesnt exists or have been used already.", 400
        l.activate()
        l.user.active = 1;
        db.session.commit()
        return "Your account have been activated", 200