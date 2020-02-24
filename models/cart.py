from in_memory import DB
from flask import session


class Cart:

    def __init__(self):
        self.products_list = {}
        self._initiate()

    def _initiate(self):
        session['cart'] = self

    @staticmethod
    def remove():
        try:
            del session['cart']
            return True
        except KeyError:
            return False

    @staticmethod
    def get_cart():
        if session.get('cart'):
            return session['cart']
