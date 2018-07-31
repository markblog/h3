from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.utils.records import Database

db = SQLAlchemy()
raw_db = Database(db)
# api = Api(prefix = '/api/v2')

"""
This should be replaced by the real redis database, so to change it conveniently, 
please keep the same grammar with redis
- token_black_list is for logout, due to the defects of the jwt
"""
redis_db = {'token_black_list':[]}

# add db model
from app.db_models import client_address_book, client_master, salesforce, billing, survey, user
from app.db_models import report, revenue_strategy, client_sentiment, business_dev_opp
from app.db_models import basic_info, engagement_strategy