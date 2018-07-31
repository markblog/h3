from app.ext import db
import datetime
from app.mixins.dict import DictMixin


class Billing(db.Model, DictMixin):

    __tablename__ = 'billing'
    
    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.String(128))
    finance_pnl_code = db.Column(db.String(128))
    client_name = db.Column(db.String(128))
    bu_division = db.Column(db.String(128))
    segment = db.Column(db.String(128))
    team_lead = db.Column(db.String(128))
    manager = db.Column(db.String(128))
    tier = db.Column(db.Integer)
    site = db.Column(db.String(128))
    cs_name_sign_off = db.Column(db.String(128))
    sign_off_date = db.Column(db.String(128))
    plan_market_value = db.Column(db.Float)
    total_value_of_service = db.Column(db.Float)
    billed = db.Column(db.Float)
    unbilled = db.Column(db.Float)
    profit_margin = db.Column(db.Float)
    update_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())

