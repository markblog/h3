import logging
from flask import Flask
from config import config
from .ext import db, Api
from app.api import search_resource as SearchResources
from app.api import report_resource as ReportResources
from app.api import PDF_resources as PDFResources
from app.api import user_resources as UserResources


def register_api(app):

    api = Api(app = app, prefix = '/api')
    api.add_resource(SearchResources.SearchListResource, '/search')
    api.add_resource(ReportResources.ReportDetailResource, '/report_detail/<report_id>')
    # api.add_resource(ReportResources.ReportResource, '/report/<client_id>/<time>')
    api.add_resource(ReportResources.ReportCompareResource, '/report_compare')
    api.add_resource(ReportResources.ReportLatestData, '/latest_data')

    api.add_resource(PDFResources.PDFPrintResource, '/print_pdf')

    api.add_resource(ReportResources.ReportNew, '/new_report')
    # api.add_resource(ReportResources.ReportChange, '/change_report/<report_id>')

    #login and logout
    api.add_resource(UserResources.LoginResource, '/login')
    api.add_resource(UserResources.LogoutResource, '/logout')
    api.add_resource(UserResources.UserListResource, '/register')

    #updated number
    api.add_resource(ReportResources.ReportupdateResource, '/update_numbers')

    #draft
    api.add_resource(ReportResources.ReportDraftList, '/drafts/<page>/<per_page>')

    api.add_resource(ReportResources.ReportDraft, '/drafts/<report_id>')

    api.add_resource(ReportResources.ReportDraftDetail, '/draft_detail/<report_id>/<previous_report_id>')

    api.add_resource(ReportResources.ReportDraftsNumber, '/drafts_number')

    api.add_resource(ReportResources.UserClientDraft, '/user_client_draft')

    # api.add_resource(ReportResources.UserClientDraftExist, '/user_client_draft_exist/<client_id>')



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    app_logging_configure(app)
    register_api(app)
    return app

def app_logging_configure(app):
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
