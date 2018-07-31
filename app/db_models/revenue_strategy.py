from app.ext import db
from app.mixins.dict import DictMixin
from sqlalchemy.dialects import postgresql


class Service(db.Model):

    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))


class ServiceDetail(db.Model):

    __tablename__ = 'service_detail'

    id = db.Column(db.Integer, primary_key=True)
    ss = db.Column(db.Boolean, default = True)
    third_party = db.Column(db.Boolean, default = True)
    revenue_strategy_id = db.Column(db.Integer, db.ForeignKey('revenue_strategy.id'))


class RevenueStrategy(DictMixin, db.Model):

    __tablename__ = 'revenue_strategy'

    id = db.Column(db.Integer, primary_key=True)
    asset_size = db.Column(db.Text)
    total_pna_revenue = db.Column(db.Text)
    direct_revenue = db.Column(db.Text)
    indirect_revenue = db.Column(db.Text)
    margin_revenue = db.Column(db.Text)
    total_ss_revenue = db.Column(db.Text)
    market_data_fees = db.Column(db.Text)
    market_data_billed = db.Column(db.Text)
    contract_ex = db.Column(db.String(64))
    overview = db.Column(db.Text)
    details = db.Column(db.Text)
    ss = db.Column(postgresql.ARRAY(db.Text))
    third_party = db.Column(postgresql.ARRAY(db.Text))
    service = db.Column(postgresql.ARRAY(db.Text))
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))