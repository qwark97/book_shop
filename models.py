import uuid
from in_memory import DB

class EBook:

    objects = DB.objects.get('EBook', {})

    def __init__(self, name, price, available, cover):
        self.id = uuid.uuid4
        self.name = name
        self.price = price
        self.available = available
        self.cover = cover


    def save(self):
        DB.insert('EBook', self)

    @staticmethod
    def all():
        return EBook.objects.values()

    def __str__(self):
        return 'Name: "%s" costs %d and is %savailable' % (
            self.name,
            self.price,
            '' if self.available else 'not '
        )

    @staticmethod
    def attributes():
        return {
            'name': str,
            'price': float,
            'available': bool,
            'cover': str,
        }