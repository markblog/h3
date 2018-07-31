# from flask_restful import Resource
from app.utils.patch import BasicResource
from flask import request, g
import datetime
from app.utils.decorators import auth
import app.services.search_services as search_services
from app.utils import time_utils as time_utils
from app.db_models.user import User


class SearchListResource(BasicResource):
    """docstring for UserResource"""
    # @auth
    def get(self):
        pass
    @auth
    def post(self):
        report_list_ret = []
        report_list = []
        data = request.get_json()
        taglist = data.get('tag_list')
        text= data.get('text')
        page = data.get('page')
        page_size = data.get('page_size')
        if not page:
            page = 1
        if not page_size:
            page_size = 10
        if taglist is None or taglist is None:
            return "taglist or text is None",400
        if len(taglist)==0:
            report_list = search_services.get_search_list_by_text(text, page, page_size)
            ret_type = 0
            for report in report_list.items:
                report_dic = {}
                report_dic['type'] = ret_type
                report_dic['client_id'] = report.client_id
                report_dic['client_name'] = report.client_name
                report_list_ret.append(report_dic)
        else:
            report_list = search_services.get_search_list_by_clientId(taglist[0]['client_id'], page, page_size)
            ret_type = 1
            filter_values = []
            timestample_dict = [(report.id, report.updated_time.strftime("%Y-%m-%d"), time_utils.datetime_to_timestamp(report.updated_time), report.author) for report in report_list.items]
            for item in timestample_dict:
                    if text in item[1]:
                        user = User.query.filter_by(id=item[3]).first()
                        filter_values.append((item[0], item[2], user.email))

            for report in filter_values:
                ret_dic = {}
                ret_dic['type'] = 1
                ret_dic['plan_date'] = report[1]
                ret_dic['report_id'] = report[0]
                ret_dic['user_name'] = report[2]
                report_list_ret.append(ret_dic)
        return report_list_ret






