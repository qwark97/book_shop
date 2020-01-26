from flask import Flask, render_template, redirect
from in_memory import DB
from tests import test_run
from app_facade.ebook_controller import EBookController
from helpers import get_all_books

app = Flask(__name__)
db = DB()


@app.route('/')
def home():
    return 'Let\' begin with Flask'


@app.route('/add-test-books')
def add_test_books():
    book_list = ['Three Body Problem', 'The Dark Forest', 'The End of Death']
    for book in book_list:
        EBookController.create(book, 80, 5)
    return "Added"


@app.route('/api/add-to-cart')
def add_to_cart():
    kwargs = {}
    return redirect('books_shelf')


@app.route('/books')
def books_shelf():
    return render_template('booksShelf.jinja', data=get_all_books()['books'])


@app.route('/test')
def test_route():
    return test_run()


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
