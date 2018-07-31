from app.ext import db
import datetime
from app.mixins.dict import DictMixin


class EngagementStrategy(db.Model, DictMixin):

    __tablename__ = 'engagement_strategy'
    
    id = db.Column(db.Integer, primary_key = True)
    executive_engagement = db.Column(db.String(128))
    executive_engagement_last_visit = db.Column(db.Text)
    cab = db.Column(db.String(128))
    client_service = db.Column(db.String(128))
    client_service_last_visit = db.Column(db.Text)
    client_service_next_visit = db.Column(db.Text)
    solutions = db.Column(db.String(128))
    solutions_last_visit = db.Column(db.Text)
    discussion = db.Column(db.Text)
    discussion_next_visit = db.Column(db.Text)
    future_engagement_plan = db.Column(db.Text)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))

