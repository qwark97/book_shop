from flask import Flask
from in_memory import DB
from tests import test_run

app = Flask(__name__)
db = DB()

@app.route('/')
def home():
    return 'Let\' begin with Flask'

@app.route('/test')
def test_route():
    test_run()


if __name__ == "__main__":
    app.run('0.0.0.0', 8080)