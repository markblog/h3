from app.ext import db
from enum import Enum
from app.mixins.dict import DictMixin
from sqlalchemy.dialects import postgresql


# class Question(db.Model):
    
#     __tablename__ = 'question'
    
#     id = db.Column(db.Integer, primary_key = True)
#     question_name = db.Column(db.String(512))
#     question_column_name = db.Column(db.String(32))

# class QuestionScore(db.Model):

#     __tablename__ = 'question_score'

#     id = db.Column(db.Integer, primary_key = True)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     client_score = db.Column(db.Float)
#     bu_score = db.Column(db.Float)
#     pna_score = db.Column(db.Float)
#     client_sentiment_id = db.Column(db.Integer, db.ForeignKey('client_sentiment.id'))


class ClientSentiment(DictMixin, db.Model):

    __tablename__ = 'client_sentiment'

    id = db.Column(db.Integer, primary_key=True)
    survey_date = db.Column(db.Text)
    sentiment_score = db.Column(db.Text)
    survey_history = db.Column(postgresql.ARRAY(db.Text))
    client_comments = db.Column(db.Text)
    strengths = db.Column(db.Text)
    weaknesses = db.Column(db.Text)
    opportunity = db.Column(db.Text)
    threats = db.Column(db.String(128))
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'))
    q = db.Column(postgresql.ARRAY(db.Text))
    rm = db.Column(postgresql.ARRAY(db.Text))
    p = db.Column(postgresql.ARRAY(db.Text))
    t1 = db.Column(db.Text)
    t2 = db.Column(db.Text)
    t3 = db.Column(db.Text)
    t4 = db.Column(db.Text)