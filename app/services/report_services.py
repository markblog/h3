from flask import g
from app.ext import raw_db
from app.db_models.billing import Billing 
from app.db_models.client_master import ClientMaster 
from app.db_models.client_address_book import ClientAddressBook
from app.db_models.client_sentiment import ClientSentiment
from app.db_models.salesforce import Salesforce 
from app.db_models.report import Report
from app.sqls.report_sqls import report_detail_sqls,report_id_sqls, auto_sqls, draft_report_detail_sqls
from app.utils.time_utils import *

from app.db_models.basic_info import BasicInfo
from app.db_models.business_dev_opp import BusinessDevOpp
from app.db_models.client_sentiment import ClientSentiment
from app.db_models.revenue_strategy import RevenueStrategy
from app.db_models.engagement_strategy import EngagementStrategy


def get_report_by_report_id(report_id):
    report = raw_db.query(report_detail_sqls, report_id=int(report_id))
    return report

def get_report_by_client_name_and_time(report_id):
    report = raw_db.query(report_id_sqls, report_id=report_id)
    return report

def get_two_compare_report(report_id, client_id):
    report = raw_db.query(report_detail_sqls, report_id=report_id)
    last_report = raw_db.query(auto_sqls, client_id=client_id)
    return report, last_report

def get_two_compare_preview_report(report_id, preview_id):
    report = raw_db.query(report_detail_sqls, report_id=report_id)
    last_report = raw_db.query(report_detail_sqls, report_id=preview_id)
    return report, last_report

def get_latest_data(client_id):
    lastest_data = raw_db.query(auto_sqls, client_id=client_id)
    return lastest_data


#++++++++++++++++++++++++++++++++++++++++++++
#drafts begin
#++++++++++++++++++++++++++++++++++++++++++++


def get_drafts_columns(report_id, previous_report_id):

    report = raw_db.query(report_detail_sqls, report_id=report_id)
    last_report = None
    if previous_report_id:
        last_report = raw_db.query(draft_report_detail_sqls, report_id=previous_report_id)
    return report, last_report


def get_source_data(client_id):

    last_report = raw_db.query(auto_sqls, client_id=client_id)
    return last_report

