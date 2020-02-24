from in_memory import DB
from flask import session
from uuid import uuid4


class Cart:

    def __init__(self):
        self.id = uuid4()
        self.products_list = {}
        self._initiate()

    def _initiate(self):
        session['cart'] = self.id
        DB.objects.update({self.id: self})

    @staticmethod
    def remove():
        try:
            del DB.objects[session['cart']]
            return True
        except KeyError:
            return False

    @staticmethod
    def get_cart():
        if session.get('cart'):
            return DB.objects[session['cart']]
