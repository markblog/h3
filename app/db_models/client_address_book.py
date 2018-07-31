from app.ext import db
import datetime
from app.mixins.dict import DictMixin


class ClientAddressBook(db.Model, DictMixin):
    
    __tablename__ = 'client_address_book'

    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.String(128))
    client_name = db.Column(db.String(1024))
    contact_name = db.Column(db.String(1024))
    contact_hierarchy = db.Column(db.String(512))
    email = db.Column(db.String(1024))
    telephone = db.Column(db.String(128))
    address1 = db.Column(db.Text)
    address2 = db.Column(db.Text)
    city = db.Column(db.String(128))
    state = db.Column(db.String(512))
    zipcode = db.Column(db.String(128))
    update_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())

