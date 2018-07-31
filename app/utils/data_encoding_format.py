import pandas as pd
from jinja2 import Environment, Template,FileSystemLoader
import re
import os

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:gxtagging@localhost/auto_plan')
# csv_path_01 = 'D:/plan automation/fake_db_data/csv/salesforce.csv'
# csv_path = 'D:/plan automation/fake_db_data/csv/billing.csv'
# csv_path= 'D:/plan automation/fake_db_data/csv/client_address_book.csv'
# csv_path= 'D:/plan automation/fake_db_data/csv/client_master.csv'
csv_path= 'D:/plan automation/fake_db_data/csv/survey.csv'


# csv_path_01 = 'D:/plan automation/fake_db_data/csv/salesforce_02.csv'
# csv_path_02 = 'D:/plan automation/fake_db_data/csv/billing_02.csv'
# csv_path_03= 'D:/plan automation/fake_db_data/csv/client_address_book_02.csv'
# csv_path_04= 'D:/plan automation/fake_db_data/csv/client_master_02.csv'
csv_path_05= 'D:/plan automation/fake_db_data/csv/survey_02.csv'
df = pd.read_csv(csv_path, encoding ='latin-1',thousands=',')
print(df.dtypes)
db_tab_cols = pd.read_sql("select * from survey", engine) \
                .columns.tolist()[1:]
print(db_tab_cols)

df.columns = db_tab_cols
df.to_sql('survey', engine, if_exists='append', index=False)

# print(df['plan_market_value'][0])
df.to_csv(csv_path_05, encoding='utf-8', index=False)


