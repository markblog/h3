# from flask import g
# from app.db_models.user import User
# from app.ext import db


# def get_user_info(user_name, password):
#     user_info = User.query.filter_by(name = user_name, password_hash = password).first()
#     return user_info

from flask import g
from app.ext import raw_db
from app.sqls import user_sqls
from app.db_models.user import User
from app.ext import db

def get_user_by_email():
    """
    query user data filter by email
    """
    user = User.query.filter_by(email = g.args.get('email')).first()
    return user

def create_user():
    """
    update user data to the database
    """
    user = User.from_dict(g.args)
    db.session.add(user)
    db.session.commit()

def get_users_except_current_user():

    users = raw_db.query(user_sqls.get_users_except_current_user, group_id = g.user.group_id, user_id = g.user.id)

    return users

def get_user_profile():

    user = User.query.get(g.user.id)

    return user