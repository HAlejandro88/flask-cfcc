from market import app
from flask import render_template
from market.models import Item


@app.route("/")
def hello_world():
    return "<h1>Hello, World! putitos</h1>"


@app.route("/about/<username>")
def about_page(username):
    return f"<h2>About page with parameter {username}</h2> "


@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
