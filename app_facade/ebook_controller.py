from models.ebook import EBook


class EBookController:

    @staticmethod
    def create(name, price, available=False, cover=''):
        ebook = EBook(
            name,
            price,
            available,
            cover
        )
        ebook.insert()
        return ebook

    @staticmethod
    def read(_id):
        """Accepts also whole EBook object"""
        if type(_id) is EBook:
            return EBook.get(_id._id)
        return EBook.get(_id)

    @staticmethod
    def update(_id, **kwargs):
        ebook = EBookController.read(_id)
        _id = ebook._id
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
