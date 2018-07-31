import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))

#Report Path
TOOL_PATH = 'D:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
HTML_PATH = 'app/PDF_print/reports/html/'
PDF_PATH = 'app/PDF_print/reports/pdf/'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '0x1092-3dfe834-324few23-342dlej'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    LOGGING_FORMAT = """[%(levelname)s] - %(asctime)s : %(message)s
%(module)s [%(pathname)s:%(lineno)d]
    """
    LOGGING_LOCATION = 'log/debug.log'
    LOGGING_LEVEL = logging.DEBUG

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://postgres:gxtagging@localhost/auto_plan'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'postgresql://postgres:gxtagging@localhost/auto_plan_test'


class ProductionConfig(Config):
    LOGGING_LOCATION = 'log/errors.log'
    LOGGING_LEVEL = logging.ERROR
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:gxtagging@localhost/auto_plan'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
