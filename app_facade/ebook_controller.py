from models.ebook import EBook
from hashlib import md5


class EBookController:

    @staticmethod
    def create(name, price, quantity=0, cover='', availability=True):
        name = str(name)
        price = float(price)
        quantity = max(0, int(quantity))
        cover = str(cover)
        availability = bool(availability)

        if EBookController._book_already_exists:
            raise Exception("Such book already exists! Try to increase its quantity")
        ebook = EBook(
            name,
            price,
            quantity,
            cover,
            availability
        )
        return ebook

    @staticmethod
    def read(id):
        """Accepts whole EBook's id or whole EBook object"""
        if type(id) is EBook:
            ebook = EBook.get(id.id)
        else:
            ebook = EBook.get(id)

        if not ebook:
            raise Exception("There is no such ebook")
        return ebook

    @staticmethod
    def update(_id, **kwargs):
        ebook = EBookController.read(_id)
        for key, val in kwargs.items():
            if ebook.__dict__.get(key, None) is None: continue
            ebook.__setattr__(key, val)
        ebook.update_state()
        return ebook

    @staticmethod
    def delete(_id):
        ebook = EBookController.read(_id)
        ebook.remove()  # co jeśli zostanie usunięta książka, która jest już w jakimś koszyku?
        return True

    @staticmethod
    def increase_quantity(id, num=1):
        ebook = EBookController.read(id)
        current_quantity = ebook.quantity
        try:
            num = int(num)
        except ValueError:
            raise Exception("You must use number to increase quantity")
        EBookController.update(id, quantity=current_quantity + num)

    @staticmethod
    def decrease_quantity(id, num=1):
        ebook = EBookController.read(id)
        current_quantity = ebook.quantity
        try:
            num = int(num)
        except ValueError:
            raise Exception("You must use number to decrease quantity")
        new_amount = current_quantity - num
        if new_amount < 0:
            raise Exception("You cannot have negative amount of books!")
        EBookController.update(id, quantity=new_amount)

    def _book_already_exists(self, name, price, cover):
        book_hash = md5(f'{name}{price}{cover}')
        return any(hash(db_book) == book_hash for db_book in EBook.get_all().items())
