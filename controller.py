from models import EBook

class EBookController:

    def create(self, name, price, available=False, cover=''):
        ebook = EBook(
            name,
            price,
            available,
            cover
        )
        ebook.save()
        return ebook.id

    def read(self, id):
        ebook = EBook.objects.get(id, None)
        return ebook

    def update(self, ebook, **kwargs):
        print(dir(EBook))
        white_list = EBook.attributes()
        new_kwargs = {}
        for attr, val in kwargs.items():
            if attr in white_list:
                new_kwargs.update(
                    (attr, white_list[attr](val))
                )

        ebook.objects.update(**new_kwargs)

    def delete(self, ebook):
        EBook.delete(ebook)

    def _add_to_dict(self, dct, key, val):
        if val:
            dct[key] = val