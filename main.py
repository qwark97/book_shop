from flask import Flask, render_template, redirect
from in_memory import DB
from tests import test_run
from app_facade.ebook_controller import EBookController
from helpers import get_all_books

app = Flask(__name__)
db = DB()


@app.route('/')
def home():
    return render_template('index.html')


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
    all_books = get_all_books()
    return render_template('booksShelf.html', data=all_books)


@app.route('/test')
def test_route():
    return test_run()


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
