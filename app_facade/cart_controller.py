from models.cart import Cart
from models.ebook import EBook
from app_facade.ebook_controller import EBookController


class CartController:

    @staticmethod
    def _create():
        cart = CartController._read()
        if not cart:
            cart = Cart()
        return cart

    @staticmethod
    def _read():
        """Accepts Cart object"""
        return Cart.get_cart()

    @staticmethod
    def get_cart():
        cart = CartController._read()
        if not cart:
            cart = CartController._create()
        return cart

    @staticmethod
    def put_in(cart, ebook, num=1):
        num = max(1, int(num))
        if type(cart) != Cart or type(ebook) != EBook:
            raise Exception("Pass valid Card and EBook objects!")
        if not cart.products_list.get(ebook.id):
            cart.products_list[ebook.id] = num
        else:
            cart.products_list[ebook.id] += num
        EBookController.decrease_quantity(ebook.id)

    @staticmethod
    def put_out(cart, ebook, num=1):
        num = max(1, int(num))
        if type(cart) != Cart or type(ebook) != EBook:
            raise Exception("Pass valid Card and EBook objects!")
        try:
            current_quantity = cart.products_list[ebook.id]
            new_quantity = current_quantity - num
            if new_quantity <= 0:
                del cart.products_list[ebook.id]
        except KeyError:
            raise Exception("This object is not in cart!")
        EBookController.increase_quantity(ebook.id)

    @staticmethod
    def delete():
        """Removes Cart object from session; True if success"""
        cart = CartController._read()
        return cart.remove()
