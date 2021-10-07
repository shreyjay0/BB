from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('main.html', title='Home')

@app.route('/shop')
def shop():
    return render_template('shop.html', title='Shop')


@app.route('/details')
def buy():
    return render_template('details.html', title='Details')

