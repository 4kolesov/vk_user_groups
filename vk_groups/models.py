from datetime import datetime

from settings import DATE_FORMAT

from . import db


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    group_id = db.Column(db.Integer)
    group_name = db.Column(db.String(250))

    def to_dict(self):
        return dict(
            id = self.id,
            query = self.query,
            timestamp = self.timestamp.strftime(DATE_FORMAT),
            group_id = self.group_id,
            group_name = self.group_name,
        )
