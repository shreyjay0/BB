from app import app
from flask import Flask, render_template, redirect
import json

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('main.html', title='Home')

@app.route('/shop')
def shop():
    products = [
  {
    "id": "s1-silk-1710",
    "name": "Cotton silk",
    "description": "Brand new multi colored",
    "img_link": "/images/saree5.jpg"
  },
  {
    "id": "s2-silk-1713",
    "name": "Cotton silk",
    "description": "Brand new multi colored",
    "img_link": "/images/saree5.jpg"
  },
  {
    "id": "s2-silk-1719",
    "name": "Cotton silk",
    "description": "Brand new multi colored",
    "img_link": "/images/saree5.jpg"
  },
  {
    "id": "s2-silk-1719",
    "name": "Cotton silk",
    "description": "Brand new multi colored",
    "img_link": "/images/saree5.jpg"
  },
  {
    "id": "s2-silk-1719",
    "name": "Cotton silk",
    "description": "Brand new multi colored",
    "img_link": "/images/saree5.jpg"
  },
  {
    "id": "s2-silk-1719",
    "name": "Cotton silk",
    "description": "Brand new multi colored",
    "img_link": "/images/saree5.jpg"
  }
]
    return render_template('shop.html', title='Shop', products=products)


@app.route('/details/<id>')
def buy(id):
    return render_template('details.html', title='Details', id=id)

@app.route('/ig')
@app.route('/instagram')
def insta():
    return redirect("https://www.instagram.com/reshamisparsh")

@app.route('/fb')
@app.route('/facebook')
def facebook():
    return redirect("https://www.facebook.com/Reshami-Sparsh-102679991652439/")

@app.route('/pinterest')
def pinterest():
    return redirect("https://www.pinterest.com/reshamisparsh")
