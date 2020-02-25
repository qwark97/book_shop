import os

from flask import Flask, render_template, request, make_response, jsonify

from app_facade.cart_controller import CartController
from in_memory import DB
from tests import test_run
from app_facade.ebook_controller import EBookController
from helpers import get_all_books

app = Flask(__name__)
db = DB()
app.secret_key = os.urandom(10)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/add-books', methods=['GET'])
def add_test_books():
    book_list = ['The Dark Forest', 'The End of Death']
    for book in book_list:
        EBookController.create(book, 80, 5)
    EBookController.create('Three Body Problem', 120, 5, 'three_body.jpg')
    EBookController.create('Dune', 100, 0, 'dune.jpg', False)
    print("Added")


@app.route('/api/add-to-cart', methods=["POST"])
def add_to_cart():
    cart_instance = CartController.get_cart()
    ebook_id = request.get_json()

    try:
        CartController.put_in(cart_instance, EBookController.read(ebook_id))
        return make_response(jsonify({"message": "OK"}), 200)
    except Exception as e:
        return make_response(jsonify({"message": e}), 404)


@app.route('/home')
def books_shelf():
    all_books = get_all_books()
    return render_template(
        'booksShelf.html',
        data=all_books
    )


@app.route('/cart')
def cart():
    get_cart_items = CartController.get_cart()
    return render_template(
        'cart.html',
        cart_items=get_cart_items
    )


@app.route('/test')
def test_route():
    return test_run()


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True)
