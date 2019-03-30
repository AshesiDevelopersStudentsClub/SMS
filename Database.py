from flask_sqlalchemy import SQLAlchemy

#DATABASE

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(250))
    quantity_left = db.Column(db.Integer)
    revenue = db.Column(db.Float)
    price = db.Column(db.Float)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    person_transacting = db.Column(db.String(250))
    item_name = db.Column(db.String(250))
    quantity_requested = db.Column(db.Integer)
    time_of_transaction = db.Column(db.String(50))
    completed = db.Column(db.Boolean)




