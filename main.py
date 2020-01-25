from flask import Flask, render_template, redirect
from in_memory import DB
from tests import test_run
from app_facade.ebook_controller import EBookController

app = Flask(__name__)
db = DB()


@app.route('/')
def home():
    return 'Let\' begin with Flask'

@app.route('/test-books')
def books():
    books = [str(book) for book in EBookController.get_all().values()]
    return str(books)

@app.route('/api/add-to-cart')
def add_to_cart():
    kwargs = {}
    return redirect('books_shelf')


@app.route('/books')
def books_shelf():
    kwargs = {}
    return render_template('booksShelf.html', **kwargs)


@app.route('/test')
def test_route():
    return test_run()


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
