from models.ebook import EBook


class EBookController:

    @staticmethod
    def create(name, price, available=False, cover='', save=True):
        ebook = EBook(
            name,
            price,
            available,
            cover
        )
        if save:
            ebook.insert()
        return ebook

    @staticmethod
    def read(_id):
        return EBook.get(_id)

    @staticmethod
    def update(_id, **kwargs):
        ebook = EBookController.read(_id)
        for key, val in kwargs.items():
            if ebook.__dict__.get(key, None) is None: continue
            ebook.__setattr__(key, val)
        ebook.update_state()

    @staticmethod
    def delete(_id):
        ebook = EBookController.read(_id)
        ebook.remove()
