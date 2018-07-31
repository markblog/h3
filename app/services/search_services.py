from flask import g
from app.ext import raw_db
from app.db_models.report import Report
from app.db_models.client_master import ClientMaster


def get_search_list_by_text(text, page = 1, per_page = 1):
    re_text = '%'+ text +'%'
    report = ClientMaster.query.filter((ClientMaster.client_name.ilike(re_text)) | (ClientMaster.client_id.ilike(re_text)))\
    .order_by(ClientMaster.update_time.desc()).paginate(page,per_page,error_out=False)
    return report


def get_search_list_by_clientId(client_id, page = 1, per_page = 2):
    report = Report.query.filter_by(client_id= client_id, status = 2).order_by(Report.updated_time.desc()).paginate(page,per_page,error_out=False)
    return report




