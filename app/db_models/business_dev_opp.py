import datetime
from sqlalchemy.dialects import postgresql
from app.ext import db
from enum import Enum
from app.mixins.dict import DictMixin


class BusinessDevOpp(DictMixin, db.Model):

    __tablename__ = 'business_dev_opp'

    id = db.Column(db.Integer, primary_key=True)
    opportunity_name = db.Column(postgresql.ARRAY(db.Text))
    probability = db.Column(postgresql.ARRAY(db.Text))
    revenue_local = db.Column(postgresql.ARRAY(db.Text))
    projected_revenue = db.Column(postgresql.ARRAY(db.Text))
    salesforceid = db.Column(db.Text)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))
