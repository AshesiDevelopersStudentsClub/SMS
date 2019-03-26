from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import sqlAlchemy
import os

app = flask(__name__)

#Route
@app.route('/')
def index():
	return "home page"

@app.route('/admin')
def admin():
	return  "admin page"

@app.route('/order')
def order():
	name = request.form['name']
	price = request.form['price']
	quantity = request.form['quantity']
	size = request.form['size']
	toppings = request.form['toppings']

	order = Order(name = name, price = price, quantity = quantity, size = size, toppings = toppings)

	db.session.add(order)
	db.session.commit()

	return redirect(url_for('index'))

@app.route('/transaction')
def transaction():
	return "transaction"


if __name__ == '__main__':
	app.run(debug = True)
