from models.cart import Cart
from models.ebook import EBook


class CartController:

    @staticmethod
    def _create(session_id):
        cart = CartController._read(session_id)
        if not cart:
            cart = Cart(session_id)
        return cart

    @staticmethod
    def _read(session_id):
        """Accepts session_id or whole Cart object"""
        if type(session_id) is Cart:
            cart = Cart.get(session_id.session_id)
        else:
            cart = Cart.get(session_id)

        return cart

    @staticmethod
    def get_cart(session_id):
        cart = CartController._read(session_id)
        if not cart:
            cart = CartController._create(session_id)
        return cart

    @staticmethod
    def put_in(cart, ebook, num=1):
        num = max(1, int(num))
        if type(cart) != Cart or type(ebook) != EBook:
            raise Exception("Pass valid Card and EBook objects!")
        if not cart.products_list.get(ebook.id, None):
            cart.products_list[ebook.id] = num
        else:
            cart.products_list[ebook.id] += num

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

    @staticmethod
    def delete(session_id):
        """Accepts session_id or whole Cart object"""
        cart = CartController._read(session_id)
        cart.remove()
        return True
