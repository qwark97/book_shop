from models.ebook import EBook


class EBookController:

    @staticmethod
    def create(name, price, quantity=0, cover=''):
        ebook = EBook(
            name,
            price,
            quantity,
            cover
        )
        return ebook

    @staticmethod
    def read(id):
        """Accepts also whole EBook object"""
        if type(id) is EBook:
            return EBook.get(id.id)
        return EBook.get(id)

    @staticmethod
    def update(_id, **kwargs):
        ebook = EBookController.read(_id)
        try:
            id = ebook.id
        except AttributeError:
            raise Exception("There is no such ebook")
        for key, val in kwargs.items():
            if ebook.__dict__.get(key, None) is None: continue
            ebook.__setattr__(key, val)
        ebook.update_state()
        return ebook

    @staticmethod
    def delete(_id):
        ebook = EBookController.read(_id)
        ebook.remove()
        return True

    @staticmethod
    def increase_quantity(id, num=1):
        ebook = EBookController.read(id)
        if not ebook: raise Exception("There is no such ebook")
        current_quantity = ebook.quantity
        EBookController.update(id, quantity=current_quantity + num)

    @staticmethod
    def decrease_quantity(id, num=1):
        ebook = EBookController.read(id)
        if not ebook: raise Exception("There is no such ebook")
        current_quantity = ebook.quantity
        new_amount = current_quantity - num
        if new_amount < 0:
            raise Exception("You cannot have negative amount of books!")
        EBookController.update(id, quantity=new_amount)
