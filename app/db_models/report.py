import datetime
from app.ext import db
from enum import Enum
from app.mixins.dict import DictMixin


class ReportStatus(Enum):

    DRAFT = 1
    POST = 2


class Report(DictMixin, db.Model):

    __tablename__ = 'report'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(128))
    client_id = db.Column(db.String(32))
    salesforce_id = db.column(db.String(32))
    updated_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    previous_report_id = db.Column(db.Integer)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer, default = ReportStatus.DRAFT.value)
