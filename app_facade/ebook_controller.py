from models.ebook import EBook


class EBookController:

    def create(self, name, price, available=False, cover='', save=True):
        ebook = EBook(
            name,
            price,
            available,
            cover
        )
        if save:
            ebook.insert()
        return ebook

    def read(self, _id):
        return EBook.get(_id)

    def update(self, _id, **kwargs):
        ebook = self.read(_id)
        for key, val in kwargs.items():
            if ebook.__dict__.get(key, None) is None: continue
            ebook.__setattr__(key, val)
        ebook.update_state()

    def delete(self, _id):
        ebook = self.read(_id)
