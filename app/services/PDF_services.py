# report services
import os, json, config, pdfkit, datetime, codecs

from flask import  render_template


def report_util(html_path, pdf_path):

    configuration = pdfkit.configuration(wkhtmltopdf=config.TOOL_PATH)
    options = {
        'orientation':'Landscape'
    }
    pdfkit.from_file(html_path, pdf_path, configuration=configuration, options = options)


def generate_report(html, name):

    now = datetime.datetime.utcnow()
    report_html_folder = config.HTML_PATH + '/' + now.strftime("%Y-%m-%d") + '/'
    report_pdf_folder  = config.PDF_PATH + '/' + now.strftime("%Y-%m-%d") + '/'
    if not os.path.exists(report_html_folder):
        os.makedirs(report_html_folder)
    if not os.path.exists(report_pdf_folder):
        os.makedirs(report_pdf_folder)

    with codecs.open(report_html_folder + name + '.html', 'w', encoding='utf-8') as f:
        f.write(html)

    report_util(report_html_folder + name + '.html', report_pdf_folder + name + '.pdf')

    return report_pdf_folder + name + '.pdf'