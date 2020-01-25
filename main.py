from flask import Flask, render_template
from in_memory import DB
from tests import test_run

app = Flask(__name__)
db = DB()


@app.route('/')
def home():
    return 'Let\' begin with Flask'


@app.route('/api/add-to-cart')
def add_to_cart():
    kwargs = {}
    return render_template('addToCart.html', **kwargs)


@app.route('/test')
def test_route():
    return test_run()


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
