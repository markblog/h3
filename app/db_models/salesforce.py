from app.ext import db
import datetime
from app.mixins.dict import DictMixin


class Salesforce(db.Model, DictMixin):
    
    __tablename__ = 'sales_force'
    
    id = db.Column(db.Integer, primary_key = True)
    account_id = db.Column(db.String(128))
    opportunity_id = db.Column(db.String(128))
    created_date = db.Column(db.String(128))
    account_name = db.Column(db.String(128))
    opportunity_name = db.Column(db.String(128))
    probability = db.Column(db.String(128))
    projected_annualized_revenue_currency = db.Column(db.String(128))
    projected_annualized_revenue = db.Column(db.String(128))
    status = db.Column(db.String(128))
    stage = db.Column(db.String(128))
    business_unit = db.Column(db.String(128))
    region = db.Column(db.String(128))
    executive_synopsis = db.Column(db.Text)
    product_family = db.Column(db.Text)
    product_name = db.Column(db.String(128))
    rollup_business_unit = db.Column(db.String(128))
    rollup_team_lead = db.Column(db.String(128))
    primary_incumbent = db.Column(db.String(128))
    decision_date = db.Column(db.String(128))
    last_modified_date = db.Column(db.String(128))
    last_modified_by = db.Column(db.String(128))
    rollup_last_comment = db.Column(db.Text)
    update_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())