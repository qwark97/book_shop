from models.cart import Cart


class CartController:

    @staticmethod
    def create(session_id):
        cart = CartController.read(session_id)
        if not cart:
            cart = Cart(session_id)
        return cart

    @staticmethod
    def read(session_id):
        """Accepts also whole Cart object"""
        if type(session_id) is Cart:
            return Cart.get(session_id.session_id)
        return Cart.get(session_id)

    @staticmethod
    def put_in(session_id, ebook):
        pass

    @staticmethod
    def put_out(session_id, ebook):
        pass

    @staticmethod
    def delete(session_id):
        cart = CartController.read(session_id)
        cart.remove()
        return True
