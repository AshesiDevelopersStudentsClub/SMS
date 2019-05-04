from flask import Flask, render_template, redirect, url_for, Response, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

from flask_simplelogin import SimpleLogin, login_required


from config import DIR


import os




app = Flask(__name__)




#DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(DIR, "database.db"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = 'something-secret'
app.config['SIMPLELOGIN_USERNAME'] = 'test'
app.config['SIMPLELOGIN_PASSWORD'] = 'test'

db = SQLAlchemy(app)

SimpleLogin(app)



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



#Route


@app.route('/')
@login_required
def index():
	transactionss = Transaction.query.order_by(Transaction.completed.desc()).all()

	return render_template('index.html', transactions=transactionss)

@app.route('/admin')
@login_required
def admin():
	return  "admin page"

@app.route('/addtransaction', methods = ['POST'])
@login_required
def addtransaction():
	item_name = request.form['item_name']
	person_transacting = request.form['person_transacting']
	quantity_requested = request.form['quantity_requested']
	time_of_transaction = datetime.now()
	completed = False

	transact = Transaction(item_name = item_name, person_transacting = person_transacting, quantity_requested = quantity_requested, time_of_transaction = time_of_transaction, completed = completed)

	db.session.add(transact)
	db.session.commit()

	return redirect(url_for('transaction'))

@app.route('/completeTransaction', methods = ['POST'])
@login_required
def completeTransaction():
	id = request.form['id']

	transact = Transaction.query.filter_by(id=id).first()

	transact.completed = True

	db.session.commit()

	return redirect(url_for("index"))

@app.route('/updateTransact', methods = ['POST'])
@login_required
def updateTransact():
	id = request.form['id']

	item_name = request.form['item_name']
	person_transacting= request.form['person_transacting']
	quantity_requested = request.form['quantity_requested']
	time_of_transaction = request.form['time_of_transaction']
	completed=request.form['completed']

	transact = Transaction.query.filter_by(id=id).first()

	db.session.commit()

	

@app.route('/addItem', methods = ['POST'])
@login_required
def addItem():
	item_name = request.form['item_name']
	quantity_left = request.form['quantity_left']
	revenue = request.form['revenue']
	price = request.form['price']

	item = Item(item_name = item_name, quantity_left = quantity_left, revenue = revenue, price = price)

	db.session.add(item)
	db.session.commit()

	return redirect(url_for('Item'))

@app.route('/updateItem', methods = ['POST'])
@login_required
def updateItem():
	id = request.form['id']

	item_name = request.form['item_name']
	quantity_left = request.form['quantity_left']
	revenue = request.form['revenue']
	price = request.form['price']

	item = Item.query.filter_by(id=id).first()

	item.item_name = item_name
	item.quantity_left = quantity_left
	item.revenue= revenue
	item.price= price


	db.session.commit()

	

@app.route('/Item')
@login_required
def item():
	return "Item page"


@app.route('/transaction')
@login_required
def transaction():
	return render_template('transaction.html')


@app.route('/restock')
@login_required
def restock():
	return render_template('restock.html')


if __name__ == '__main__':
	app.run(debug = True)
