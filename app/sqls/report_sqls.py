auto_sqls = """
   SELECT b.plan_market_value,
                 cm.client_name,
                 cm.client_id,
                 cab.address1,
                 cab.city,
                 cab.state as country_state,
                 cab.zipcode,
                 cm.clientstartdate,
                 cm.bu_division,
                 cm.segment,
                 cm.mktsubsegment,
                 cm.bu_relationship_managers,
                 cm.tier,
                 cm.auditlocation,
                 cm.site_lead,
                 cab.contact_name as primary_contact_name,
                 cab.email as primary_contact_email,
                 cab.telephone as primary_contack_tel,
                 b.plan_market_value,
                 b.total_value_of_service,
                 b.billed, 
                 b.unbilled, 
                 b.profit_margin,
                 survey.q1,
                 survey.q2,
                 survey.q3, 
                 survey.q4, 
                 survey.q5,
                 survey.rm1,
                 survey.rm2,
                 survey.rm3,
                 survey.rm4,
                 survey.rm5,
                 survey.p1,
                 survey.p2,
                 survey.p3,
                 survey.p4,
                 survey.p5,
                 survey.t1,
                 survey.t2,
                 survey.t3,
                 survey.t4,
                 survey.comment as client_comments,
                 cm.salesforceid,
                 sf.opportunity_name,
                 sf.probability,
                 sf.projected_annualized_revenue_currency as revenue_local,
                 sf.projected_annualized_revenue as projected_revenue
            FROM public.client_master as cm 
            LEFT JOIN public.billing as b ON cm.client_id = b.client_id 
            LEFT JOIN public.survey as survey ON cm.client_id = survey.client_id
            LEFT JOIN public.client_address_book as cab ON cm.client_id = cab.client_id
            LEFT JOIN public.salesforce sf ON cm.salesforceid = sf.account_id
            WHERE cm.client_id= :client_id 
            ORDER BY cm.update_time DESC 
            LIMIT 1
"""



report_detail_sqls = """
SELECT  r.client_name as client_name,
        r.client_id as client_id,
        FLOOR(EXTRACT(EPOCH FROM r.updated_time))* 1000 as showtime,
        address1,
        city,
        state as country_state,
        zipcode,
        client_start_date,
        executive_summary,
        bu_division,
        segment,
        sub,
        bu_relationship_managers,
        coo,
        ss_top_50,
        tier,
        core_ops_auditlocation,
        pna_team_lead_site_lead,
        pna_lead,
        pna_last_visit,
        senior_contact_name,
        senior_contact_email,
        senior_contact_tel,
        primary_contact_name,
        primary_contact_email,
        primary_contact_tel,
        isa_portal,
        pna_watchlist,
        since,
        late_deliverables_qtr,
        error_memos_qstrs,
        asset_size,
        total_pna_revenue,
        direct_revenue,
        indirect_revenue,
        margin_revenue,
        total_ss_revenue,
        market_data_fees,
        market_data_billed,
        contract_ex, 
        overview,
        details,
        executive_engagement,
        executive_engagement_last_visit,
        cab,
        client_service, 
        client_service_last_visit,
        client_service_next_visit,
        solutions,
        solutions_last_visit,
        discussion,
        discussion_next_visit,
        future_engagement_plan,
        sentiment_score,
        survey_date,
        survey_history,
        client_comments,
        weaknesses,
        strengths,
        opportunity,
        threats,
        opportunity_name,
        probability,
        projected_revenue,
        revenue_local,
        cs.q[1] as q1,
        cs.q[2] as q2,
        cs.q[3] as q3,
        cs.q[4] as q4,
        cs.q[5] as q5,
        cs.rm[1] as rm1,
        cs.rm[2] as rm2,
        cs.rm[3] as rm3,
        cs.rm[4] as rm4,
        cs.rm[5] as rm5,
        cs.p[1] as p1,
        cs.p[2] as p2,
        cs.p[3] as p3,
        cs.p[4] as p4,
        cs.p[5] as p5,
        cs.t1,
        cs.t2,
        cs.t3,
        cs.t4,
        rs.service,
        rs.ss,
        rs.third_party,
        bdo.salesforceid

    FROM public.report as r
    LEFT JOIN public.basic_info as bi on bi.report_id = r.id
    LEFT JOIN public.business_dev_opp as bdo on bdo.report_id = r.id
    LEFT JOIN public.client_sentiment as cs on cs.report_id = r.id
    LEFT JOIN public.revenue_strategy as rs on rs.report_id = r.id
    LEFT JOIN public.engagement_strategy as s on s.report_id = r.id
    WHERE r.id = :report_id
"""



report_id_sqls = """
SELECT id 
FROM public.report 
-- WHERE client_id = :client_id and date_trunc('second', updated_time) = timestamp :time
WHERE id = :report_id
    """

question_scores_by_report_id = """
SELECT id 
FROM public.report 
WHERE client_id = :client_id and updated_time = :time 
    """




insert_report = """
INSERT INTO public.report(
            client_name,
            client_id,
            updated_time,
            previous_report_id, 
            author,
            status)
            VALUES
            (
            :client_name,
            :client_id,
            :updated_time,
            :previous_report_id, 
            :author,
            :status)
            RETURNING id
    """


insert_basic_info = """
INSERT INTO public.basic_info(
       client_name,
       address1,
       city,
       state,
       zipcode,
       client_start_date, 
       executive_summary,
       bu_division,
       segment,
       sub,
       bu_relationship_managers, 
       coo,
       ss_top_50,
       tier,
       core_ops_auditlocation,
       pna_team_lead_site_lead, 
       pna_lead,
       pna_last_visit,
       senior_contact_name,
       senior_contact_email, 
       senior_contact_tel,
       primary_contact_name,
       primary_contact_email, 
       primary_contact_tel,
       isa_portal,
       pna_watchlist,
       since,
       late_deliverables_qtr, 
       error_memos_qstrs,
       report_id)
       VALUES
       (
       :client_name,
       :address1,
       :city,
       :state,
       :zipcode, 
       :client_start_date, 
       :executive_summary,
       :bu_division,
       :segment,
       :sub,
       :bu_relationship_managers, 
       :coo,
       :ss_top_50,
       :tier,
       :core_ops_auditlocation,
       :pna_team_lead_site_lead, 
       :pna_lead, pna_last_visit,
       :senior_contact_name,
       :senior_contact_email, 
       :senior_contact_tel,
       :primary_contact_name,
       :primary_contact_email, 
       :primary_contact_tel,
       :isa_portal, 
       :pna_watchlist,
       :since,
       :late_deliverables_qtr, 
       :error_memos_qstrs,
       :report_id)
    """


insert_business_dev_opp = """
INSERT INTO public.business_dev_opp(
            opportunity_name,
            probability,
            projected_revenue,
            report_id, 
            revenue_local),
            VALUES
            (
            :opportunity_name,
            :probability,
            :projected_revenue,
            :report_id, 
            :revenue_local
            )
    """


insert_client_sentiment = """
INSERT INTO public.client_sentiment(
            survey_date,
            sentiment_score,
            survey_history,
            client_comments, 
            strengths,
            weaknesses,
            opportunity,
            threats,
            report_id,
            q,
            rm, 
            ps)
            VALUES
            (
            :survey_date,
            :sentiment_score,
            :survey_history,
            :client_comments, 
            :strengths,
            :weaknesses,
            :opportunity,
            :threats,
            :report_id,
            :q,
            :rm, 
            :ps
            )
    """

insert_revenue_strategy = """
INSERT INTO public.revenue_strategy(
            asset_size,
            total_pna_revenue,
            direct_revenue,
            indirect_revenue,
            margin_revenue,
            total_ss_revenue,
            market_data_fees,
            market_data_billed, 
            contract_ex,
            overview,
            details,
            report_id,
            ss,
            third_party,
            service)
            VALUES
            (
            :asset_size,
            :total_pna_revenue,
            :direct_revenue,
            :indirect_revenue,
            :margin_revenue,
            :total_ss_revenue,
            :market_data_fees,
            :market_data_billed, 
            :contract_ex,
            :overview,
            :details,
            :report_id,
            :ss,
            :third_party,
            :service
            ) 
    """

insert_engagement_strategy = """
INSERT INTO public.engagement_strategy(
                              executive_engagement,
                              executive_engagement_last_visit,
                              cab, 
                              client_service,
                              client_service_last_visit,
                              client_service_next_visit, 
                              solutions,
                              solutions_last_visit,
                              discussion,
                              discussion_next_visit, 
                              future_engagement_plan,
                              report_id)
            VALUES
            (
              :executive_engagement,
              :executive_engagement_last_visit,
              :cab, 
              :client_service,
              :client_service_last_visit,
              :client_service_next_visit, 
              :solutions,
              :solutions_last_visit,
              :discussion,
              :discussion_next_visit, 
              :future_engagement_plan,
              :report_id
            )
    """


# question_scores = """
# SELECT  r.client_name,
#         address1,
#         city,
#         state,
#         zipcode,
#         client_start_date,
#         executive_summary,
#         bu_division,
#         segment,
#         sub,
#         bu_relationship_managers,
#         coo,
#         ss_top_50,
#         tier,
#         core_ops_auditlocation,
#         pna_team_lead_site_lead
#  FROM public.report as r
#                    LEFT JOIN public.basic_info as bi on bi.report_id = r.id
#                    LEFT JOIN public.business_dev_opp as bdo on bdo.report_id = r.id
#                    LEFT JOIN public.client_sentiment as cs on cs.report_id = r.id
#                    LEFT JOIN public.revenue_strategy as rs on rs.report_id = r.id
#                    LEFT JOIN public.engagement_strategy as s on s.report_id = r.id



# question_scores_by_report_id = """
# SELECT id 
# FROM public.report 
# WHERE client_id = :client_id and updated_time = :time 
#     """


#drafts begin






draft_report_detail_sqls = """
SELECT  r.client_name as client_name,
        r.client_id as client_id,
        FLOOR(EXTRACT(EPOCH FROM r.updated_time))* 1000 as showtime,
        address1,
        city,
        state as country_state,
        zipcode,
        client_start_date,
        executive_summary,
        bu_division,
        segment,
        sub,
        bu_relationship_managers,
        coo,
        ss_top_50,
        tier,
        core_ops_auditlocation,
        pna_team_lead_site_lead,
        pna_lead,
        pna_last_visit,
        senior_contact_name,
        senior_contact_email,
        senior_contact_tel,
        primary_contact_name,
        primary_contact_email,
        primary_contact_tel,
        isa_portal,
        pna_watchlist,
        since,
        late_deliverables_qtr,
        error_memos_qstrs,
        asset_size,
        total_pna_revenue,
        direct_revenue,
        indirect_revenue,
        margin_revenue,
        total_ss_revenue,
        market_data_fees,
        market_data_billed,
        contract_ex, 
        overview,
        details,
        executive_engagement,
        executive_engagement_last_visit,
        cab,
        client_service, 
        client_service_last_visit,
        client_service_next_visit,
        solutions,
        solutions_last_visit,
        discussion,
        discussion_next_visit,
        future_engagement_plan,
        sentiment_score,
        survey_date,
        survey_history,
        client_comments,
        weaknesses,
        strengths,
        opportunity,
        threats,
        opportunity_name,
        probability,
        projected_revenue,
        revenue_local,
        cs.q[1] as q1,
        cs.q[2] as q2,
        cs.q[3] as q3,
        cs.q[4] as q4,
        cs.q[5] as q5,
        cs.rm[1] as rm1,
        cs.rm[2] as rm2,
        cs.rm[3] as rm3,
        cs.rm[4] as rm4,
        cs.rm[5] as rm5,
        cs.p[1] as p1,
        cs.p[2] as p2,
        cs.p[3] as p3,
        cs.p[4] as p4,
        cs.p[5] as p5,
        rs.service,
        rs.ss,
        rs.third_party
    FROM public.report as r
    LEFT JOIN public.basic_info as bi on bi.report_id = r.id
    LEFT JOIN public.business_dev_opp as bdo on bdo.report_id = r.id
    LEFT JOIN public.client_sentiment as cs on cs.report_id = r.id
    LEFT JOIN public.revenue_strategy as rs on rs.report_id = r.id
    LEFT JOIN public.engagement_strategy as s on s.report_id = r.id

 WHERE r.id = :report_id
"""


client_master_sql = """
SELECT FLOOR(EXTRACT(EPOCH FROM update_time))* 1000 as data_showtime
FROM public.client_master
WHERE client_id = :client_id
"""