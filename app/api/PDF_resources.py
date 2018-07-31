
from app.utils.patch import BasicResource
from flask import  jsonify, request, send_file
from flask_restful import reqparse
from app.services import PDF_services as PDFServices

import config
import os
import time
import datetime
import json

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('html')


class PDFPrintResource(BasicResource):

    # @authenticate
    # def get(self, user):
    #     report = Report.query.filter_by(id = id).first()
    #     # Here need to remove the 'app' from the path for show the pdf. send_file is a relative function will figure
    #     # out in the future
    #     return send_file(report.path.replace('app/',''), mimetype = 'application/pdf')


    # @authenticate
    def post(self):
        # todo: save pdf in backend

        try:
            args = parser.parse_args()
            html = args['html']
            name = args['name']
            path = PDFServices.generate_report(html, name)

            return send_file(path.replace('app/',''), mimetype = 'application/pdf')

        except Exception as e:
            print(str(e))
            self.response_dic['code'] = 500
            self.response_dic['message'] = 'A error occured here'

        return jsonify(self.response_dic)
