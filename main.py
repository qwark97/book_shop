import os

from flask import Flask, render_template, redirect, session
from in_memory import DB
from tests import test_run
from app_facade.ebook_controller import EBookController
from app_facade.cart_controller import CartController
from helpers import get_all_books

app = Flask(__name__)
db = DB()
app.secret_key = os.urandom(10)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add-test-books')
def add_test_books():
    book_list = ['The Dark Forest', 'The End of Death']
    for book in book_list:
        EBookController.create(book, 80, 5)
    EBookController.create('Three Body Problem', 120, 5, 'three_body.jpg')
    EBookController.create('Dune', 100, 0, 'dune.jpg', False)
    return "Added"


@app.route('/api/add-to-cart')
def add_to_cart():
    kwargs = {}
    return redirect('books_shelf')


@app.route('/home')
def books_shelf():
    all_books = get_all_books()
    return render_template('booksShelf.html', data=all_books)


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/test')
def test_route():
    return test_run()


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
