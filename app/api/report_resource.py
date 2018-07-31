from app.services import report_services
from app.utils.patch import BasicResource
from flask import request, g
from app.ext import db
from app.db_models.basic_info import BasicInfo
from app.db_models.report import Report
from app.db_models.business_dev_opp import BusinessDevOpp
from app.db_models.client_sentiment import ClientSentiment
from app.db_models.revenue_strategy import RevenueStrategy
from app.db_models.client_master import ClientMaster
from app.utils.decorators import auth
from app.db_models.engagement_strategy import EngagementStrategy
import datetime
import traceback
import sys
from app.utils import time_utils as time_utils
from app.sqls.report_sqls import client_master_sql
from app.ext import raw_db
from app.db_models.user import User




class ReportDetailResource(BasicResource):
    @auth
    def get(self, report_id):
        r_dic = report_services.get_report_by_report_id(report_id)
        r_dic = r_dic.to_dict()
        user = User.query.filter_by(id = g.user.id).first()
        r_dic.append({"user_name":user.email}) 
        return r_dic

class ReportResource(BasicResource):

    @auth
    def get(self, report_id):
        pass


# class ReportCompareTwoColumnResource(BasicResource):
#     @auth
#     def get(self):
#         pass
#     @auth
#     def post(self):
#         data = request.get_json()
#         report_id = data.get('report_id')
#         r_dic = report_services.get_compare_two_clomn_by_report_id(client_id, plan_date)
#         return r_dic.to_dict()


class ReportCompareResource(BasicResource):
    @auth
    def get(self):
        ret_dic = {}
        client_id = request.args.get('client_id')
        report_id = request.args.get('report_id')


        report, last_report = report_services.get_two_compare_report(report_id, client_id)
        ret_dic['tab_time'] = report.to_dict()
        ret_dic['tab_latest'] = last_report.to_dict()
        return ret_dic


# to do
# class ReportCompareDiffNumsResource(BasicResource):
#     @auth
#     def get(self, report_id, client_id):
#         ret_dic = {}
#         report, last_report = report_services.get_two_compare_report(report_id, client_id)
#         ret_dic['tab_time'] = report.to_dict()
#         ret_dic['tab_latest'] = last_report.to_dict()
#         return ret_dic


class ReportupdateResource(BasicResource):
    @auth
    def get(self):
        client_id = request.args.get('client_id')
        report_id = request.args.get('report_id')
        numbers = diff_number(report_id, client_id)
        return numbers

def diff_number(report_id, client_id):

        report, last_report = report_services.get_two_compare_report(report_id, client_id)
        report_dic = report.to_dict()
        last_report = last_report.to_dict()

        numbers = 0
        if last_report is not None and report_dic is not None:
            for k,v in last_report[0].items():
                for r_k, r_v in report_dic[0].items():
                    if k == r_k and v is not None and r_v is not None:
                        if str(v).strip() != str(r_v).strip():
                            print(v)
                            print("*************************")
                            print(r_v)
                            numbers = numbers + 1
        return numbers


class ReportLatestData(BasicResource):
    @auth
    def get(self):
        client_id = request.args.get('client_id')
        data = report_services.get_latest_data(client_id)
        return data.to_dict()


class ReportNew(BasicResource):
    @auth
    def post(self):
        data = request.get_json()
        r_data = data[0]['data']
        b_data = data[1]['data']
        rs_data = data[2]['data']
        es_data = data[3]['data']
        cs_data = data[4]['data']
        dbo_data = data[5]['data']
        # report_id = data[6]['report_id']
        draft = data[7]['draft']
        previous_report_id = data[8]['previous_report_id']
        user = g.user
        try:
            if draft is True:
                # r_data['salesforce_id'] = None
                r_data['updated_time'] = datetime.datetime.utcnow()
                r_data['previous_report_id'] = previous_report_id
                r_data['author'] = user.id
                r_data['status'] = 3
                r = Report(**r_data)
                db.session.add(r)
                db.session.flush()
            else:
                # r_data['salesforce_id'] = None
                r_data['updated_time'] = datetime.datetime.utcnow()
                r_data['previous_report_id'] = previous_report_id
                r_data['author'] = user.id
                r_data['status'] = 2
                r = Report(**r_data)
                db.session.add(r)
                db.session.flush()
            # else:
            #     # r_data['salesforce_id'] = None
            #     r_data['updated_time'] = datetime.datetime.utcnow()
            #     r_data['previous_report_id'] = None
            #     r_data['author'] = user.id
            #     r_data['status'] = 1
            #     r = Report(**r_data)
            #     db.session.add(r)
            #     db.session.flush()

            dbo_data['report_id'] = r.id
            es_data['report_id'] = r.id
            rs_data['report_id'] = r.id
            b_data['report_id'] = r.id
            cs_data['report_id'] = r.id

            b = BasicInfo(**b_data)
            rs = RevenueStrategy(**rs_data)
            es = EngagementStrategy(**es_data)
            cs = ClientSentiment(**cs_data)
            dbo = BusinessDevOpp(**dbo_data)
            db.session.add(b)
            db.session.flush()
            db.session.add(rs)
            db.session.flush()
            db.session.add(es)
            db.session.flush()
            db.session.add(cs)
            db.session.flush()
            db.session.add(dbo)
            db.session.flush()
            db.session.commit()
        except Exception:
            db.session.rollback()
            traceback.print_exc()
            return "save failed!"
        return {'report_id': r.id}

    @auth
    def put(self):
        data = request.get_json()
        # r_data = data[0]['data']
        b_data = data[1]['data']
        rs_data = data[2]['data']
        es_data = data[3]['data']
        cs_data = data[4]['data']
        dbo_data = data[5]['data']
        report_id = data[6]['report_id']
        # draft = data[7]['draft']
        previous_report_id = data[8]['previous_report_id']
        user = g.user
        try:
            r=Report.query.filter_by(id=report_id).first()
            r.previous_report_id = previous_report_id
            r.updated_time = datetime.datetime.utcnow()
            r.author = user.id
            db.session.add(r)
            db.session.flush()
            basic_info=BasicInfo.query.filter_by(report_id=report_id).first()
            basic_info.address1 = b_data.get("address1")
            basic_info.city = b_data.get("city")
            basic_info.state = b_data.get("state")
            basic_info.zipcode =b_data.get("zipcode")
            basic_info.client_start_date =b_data.get("client_start_date")
            basic_info.executive_summary = b_data.get("executive_summary")
            basic_info.bu_division = b_data.get("bu_division")
            basic_info.segment = b_data.get("segment")
            basic_info.sub =b_data.get("sub")
            basic_info.bu_relationship_managers = b_data.get("bu_relationship_managers")
            basic_info.coo = b_data.get("coo")
            basic_info.ss_top_50 = b_data.get("ss_top_50")
            basic_info.tier = b_data.get("tier")
            basic_info.core_ops_auditlocation = b_data.get("core_ops_auditlocation")
            basic_info.pna_team_lead_site_lead = b_data.get("pna_team_lead_site_lead")
            basic_info.pna_lead = b_data.get("pna_lead")
            basic_info.pna_last_visit = b_data.get("pna_last_visit")
            basic_info.senior_contact_name = b_data.get("senior_contact_name")
            basic_info.senior_contact_email = b_data.get("senior_contact_email")
            basic_info.senior_contact_tel = b_data.get("senior_contact_tel")
            basic_info.primary_contact_name = b_data.get("primary_contact_name")
            basic_info.primary_contact_email = b_data.get("primary_contact_email")
            basic_info.primary_contact_tel = b_data.get("primary_contact_tel")
            basic_info.isa_portal = b_data.get("isa_portal")
            basic_info.pna_watchlist = b_data.get("pna_watchlist")
            basic_info.since = b_data.get("since")
            basic_info.late_deliverables_qtr = b_data.get("late_deliverables_qtr")
            basic_info.error_memos_qstrs = b_data.get("error_memos_qstrs")

            revenue_strategy=RevenueStrategy.query.filter_by(report_id=report_id).first()
            revenue_strategy.asset_size = rs_data.get("asset_size")
            revenue_strategy.total_pna_revenue = rs_data.get("asset_size")
            revenue_strategy.direct_revenue = rs_data.get("direct_revenue")
            revenue_strategy.indirect_revenue = rs_data.get("indirect_revenue")
            revenue_strategy.margin_revenue = rs_data.get("margin_revenue")
            revenue_strategy.total_ss_revenue = rs_data.get("total_ss_revenue")
            revenue_strategy.total_pna_revenue = rs_data.get("total_pna_revenue")
            revenue_strategy.market_data_fees = rs_data.get("market_data_fees")
            revenue_strategy.market_data_billed = rs_data.get("market_data_billed")
            revenue_strategy.contract_ex = rs_data.get("contract_ex")
            revenue_strategy.overview = rs_data.get("overview")
            revenue_strategy.details = rs_data.get("details")
            revenue_strategy.ss = rs_data.get("ss")
            revenue_strategy.third_party = rs_data.get("third_party")
            revenue_strategy.service = rs_data.get("service")


            engagementstrategy=EngagementStrategy.query.filter_by(report_id=report_id).first()
            engagementstrategy.executive_engagement = es_data.get("executive_engagement")
            engagementstrategy.executive_engagement_last_visit = es_data.get("executive_engagement_last_visit")
            engagementstrategy.cab = es_data.get("cab")
            engagementstrategy.client_service = es_data.get("client_service")
            engagementstrategy.client_service_last_visit = es_data.get("client_service_last_visit")
            engagementstrategy.client_service_next_visit = es_data.get("client_service_next_visit")
            engagementstrategy.solutions = es_data.get("solutions")
            engagementstrategy.solutions_last_visit = es_data.get("solutions_last_visit")
            engagementstrategy.discussion = es_data.get("discussion")
            engagementstrategy.discussion_next_visit = es_data.get("discussion_next_visit")
            engagementstrategy.future_engagement_plan = es_data.get("future_engagement_plan")


            clientsentiment=ClientSentiment.query.filter_by(report_id=report_id).first()
            clientsentiment.survey_date = cs_data.get("survey_date")
            clientsentiment.sentiment_score = cs_data.get("sentiment_score")
            clientsentiment.survey_history = cs_data.get("survey_history")
            clientsentiment.client_comments = cs_data.get("client_comments")
            clientsentiment.strengths = cs_data.get("strengths")
            clientsentiment.weaknesses = cs_data.get("weaknesses")
            clientsentiment.opportunity = cs_data.get("opportunity")
            clientsentiment.threats = cs_data.get("threats")
            clientsentiment.q = cs_data.get("q")
            clientsentiment.rm = cs_data.get("rm")
            clientsentiment.p = cs_data.get("p")

            businessdevopp=BusinessDevOpp.query.filter_by(report_id=report_id).first()
            businessdevopp.opportunity_name = dbo_data.get("opportunity_name")
            businessdevopp.probability = dbo_data.get("probability")
            businessdevopp.revenue_local = dbo_data.get("revenue_local")
            businessdevopp.projected_revenue = dbo_data.get("projected_revenue")
            businessdevopp.salesforceid = dbo_data.get("salesforceid")


            db.session.add(basic_info)
            db.session.flush()
            db.session.add(revenue_strategy)
            db.session.flush()
            db.session.add(engagementstrategy)
            db.session.flush()
            db.session.add(clientsentiment)
            db.session.flush()
            db.session.add(businessdevopp)
            db.session.flush()
            db.session.commit()
        except Exception:
            db.session.rollback()
            traceback.print_exc()
            return "update failed!"
        return "update success!"


# class ReportChange(BasicResource):

#     @auth
#     def get(self, report_id):
#         r=Report.query.filter_by(id=report_id).first()
#         try:
#             r.status  = 2
#             db.session.add(r)
#             db.session.commit()
#         except Exception as err:
#             db.session.rollback()
#             traceback.print_exc()
#         return "status change success!"


class ReportDraftList(BasicResource):

    @auth
    def get(self, page, per_page):
        ret_dic = []
        reports = Report.query.filter_by(status = 3, author = g.user.id).order_by(Report.updated_time.desc()).paginate(int(page),int(per_page),error_out=False)
        for report in reports.items:
            temp_dic = {}
            temp_dic['report_id'] = report.id
            if report.previous_report_id == None:
                report.previous_report_id = "0"
            _,temp_dic['color_flag'] = check_drafts_detail(report.id, report.previous_report_id)
            temp_dic['client_name'] = report.client_name
            temp_dic['update_time'] = time_utils.datetime_to_timestamp(report.updated_time)
            temp_dic['previous_report_id'] = report.previous_report_id
            ret_dic.append(temp_dic)
        return ret_dic


class ReportDraftDetail(BasicResource):

    @auth
    def get(self, report_id, previous_report_id):
        ret_dic,_ = check_drafts_detail(report_id, previous_report_id)
        return ret_dic


class ReportDraft(BasicResource):

    @auth
    def delete(self, report_id):
        report = Report.query.filter_by(id = report_id, author = g.user.id).first()
        report.status = 4
        try:
            db.session.add(report)
            db.session.commit()
            return "delete successful!"
        except:
            db.session.rollback()
            return "delete failed"

def check_drafts_detail(report_id, previous_report_id):
    ret_dic = {}
    client_id = None
    showtime = None
    red_flag = False

    if int(previous_report_id) != 0:
        report, last_report = report_services.get_drafts_columns(report_id, previous_report_id)
        for i in report:
            client_id = i.client_id
        for i in report:
            showtime = i.showtime
        client_master = raw_db.query(client_master_sql, client_id=client_id).first()

        if client_master.data_showtime > showtime:
            last_last_report = report_services.get_source_data(client_id)

            red_flag = change_color(report_id, client_id, red_flag)
            if red_flag:
                ret_dic['tab_latest_latest'] = last_last_report.to_dict()
        ret_dic['tab_time'] = last_report.to_dict()
        ret_dic['tab_latest'] = report.to_dict()
    else:
        report, _ = report_services.get_drafts_columns(report_id, previous_report_id)
        for i in report:
            client_id = i.client_id
            showtime = i.showtime

        client_master = raw_db.query(client_master_sql, client_id=client_id).first()

        if client_master.data_showtime > showtime:
            last_last_report = report_services.get_source_data(client_id)
            # ret_dic['tab_latest'] = last_last_report.to_dict()
            red_flag = change_color(report_id, client_id, red_flag)
            if red_flag:
                ret_dic['tab_latest'] = last_last_report.to_dict()

        ret_dic['tab_time'] = report.to_dict()
    return ret_dic, red_flag

def change_color(report_id, client_id, red_flag):
    number = diff_number(report_id, client_id)
    if number > 0:
        red_flag = True
    return red_flag


class ReportDraftsNumber(BasicResource):

    @auth
    def get(self):
        numbers = Report.query.filter_by(status = 3, author = g.user.id).count()
        return numbers


class UserClientDraft(BasicResource):

    @auth
    def get(self):
        client_id = request.args.get('client_id')
        ret_dic = {}
        report = Report.query.filter_by(client_id = client_id, author = g.user.id, status = 3).first()
        user = User.query.filter_by(id=g.user.id).first()
        if report is None:
            ret_dic['report_id'] = None
            ret_dic['previous_report_id'] = None
            ret_dic['showtime'] = None
            ret_dic['user_name'] = user.email
        else:
            ret_dic['report_id'] = report.id
            ret_dic['previous_report_id'] = report.previous_report_id
            ret_dic['showtime'] = time_utils.datetime_to_timestamp(report.updated_time)
            ret_dic['user_name'] = user.email
        return ret_dic


# class UserClientDraftExist(BasicResource):

#     @auth
#     def get(self, client_id):
#         report_id = None
#         report = Report.query.filter_by(client_id = client_id, author = g.user.id, status = 3).first()
#         if report:
#             report_id = report.id
#         return report_id
