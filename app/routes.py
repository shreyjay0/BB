from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return app.send_static_file('main.html', title="Home")

@app.route('/shop')
def index():
    return app.send_static_file('shop.html', title="Shop")


@app.route('/buy')
def index():
    return app.send_static_file('buy.html', title="Buy")
