from app.ext import db
import datetime
from app.mixins.dict import DictMixin


class BasicInfo(db.Model, DictMixin):

    __tablename__ = 'basic_info'

    id = db.Column(db.Integer, primary_key = True)
    client_name = db.Column(db.String(512))
    address1 = db.Column(db.String(1024))
    city = db.Column(db.String(128))
    state = db.Column(db.String(128))
    zipcode = db.Column(db.String(128))
    client_start_date = db.Column(db.Text)
    executive_summary = db.Column(db.Text)
    bu_division = db.Column(db.String(64))
    segment = db.Column(db.String(128))
    sub = db.Column(db.String(128))
    bu_relationship_managers = db.Column(db.String(128))
    coo = db.Column(db.String(128))
    ss_top_50 = db.Column(db.String(128))
    tier = db.Column(db.Text)
    core_ops_auditlocation = db.Column(db.String(128))
    pna_team_lead_site_lead = db.Column(db.String(128))
    pna_lead = db.Column(db.String(128))
    pna_last_visit = db.Column(db.Text)
    senior_contact_name = db.Column(db.String(1024))
    senior_contact_email = db.Column(db.String(1024))
    senior_contact_tel = db.Column(db.String(128))
    primary_contact_name = db.Column(db.String(1024))
    primary_contact_email = db.Column(db.String(1024))
    primary_contact_tel = db.Column(db.String(128))
    isa_portal = db.Column(db.String(128))
    pna_watchlist = db.Column(db.String(128))
    since = db.Column(db.Text)
    late_deliverables_qtr = db.Column(db.Text)
    error_memos_qstrs = db.Column(db.Text)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))





