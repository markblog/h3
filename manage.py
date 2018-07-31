#!/usr/bin/env python
import os, random
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import g, render_template
from werkzeug.local import LocalProxy
from flask_cors import CORS
import pandas as pd
from jinja2 import Environment, Template, FileSystemLoader
import re
import os
from app.utils import file_utils
from config import config
import datetime
from sqlalchemy import create_engine
from jinja2 import Template
from flask_script import Manager,Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
CORS(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver',
                    Server(use_debugger = True,use_reloader = True,port=4000)) 


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



""""latin-64 is required if it has some encoding problem.
    you can also change the encoding to utf-8 if you format the data source""" 
@manager.command
def import_data(f_type="excel", encoding="utf-8"):
    """import data from excel or csv."""

    base_dir = os.path.abspath(os.path.dirname(__file__))
    csv_base_path = base_dir + "/db_data/csv"  
    excel_base_path = base_dir + "/db_data/excel"
    db_config = config['default'].SQLALCHEMY_DATABASE_URI
    engine = create_engine(db_config)
    dfs = []
    if f_type == 'csv':
        csv_paths = file_utils.get_current_dir_files(csv_base_path)
        dfs = file_utils.get_dataframe_from_csv(csv_paths, encoding)
    else:
        excel_file = file_utils.get_current_dir_first_file(excel_base_path)
        dfs = file_utils.get_dataframes_from_excel(excel_file, encoding)
    
    for name, df in dfs.items():

        sql = "select * from " + name + ' limit 1'
        db_tab_cols = pd.read_sql(sql, engine).columns.tolist()
        # df['id'] = pd.Series(2, index=df.index)
        df['update_time'] = pd.Series(datetime.datetime.utcnow(), index=df.index)
        # print(df['update_time'])

        df.columns = db_tab_cols
        print(df.columns)

        df.to_sql(name, engine, if_exists='append', index=False)


if __name__ == '__main__':
    manager.run()
