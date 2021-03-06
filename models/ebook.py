import uuid
from in_memory import DB


class EBook:

    def __init__(self, name, price, quantity, cover, availability):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.quantity = quantity
        self.cover = cover
        self.availability = availability
        self._insert()

    def __str__(self):
        return f'Book: "{self.name}" with id: {self.id}. Availability: {self.available}'

    def __hash__(self):
        return hash(f'{self.name}{self.price}{self.cover}')

    def _insert(self):
        if not DB.objects.get('EBook', None):
            DB.objects['EBook'] = {}
        DB.objects['EBook'][self.id] = self

    @staticmethod
    def get(id):
        if DB.objects.get('EBook', {}):
            return DB.objects.get('EBook', {}).get(id, None)

    @staticmethod
    def get_all():
        return DB.objects.get('EBook', {})

    @property
    def available(self):
        return bool(self.get_all()) and self.availability

    def update_state(self):
        self._insert()

    def remove(self):
        del DB.objects['EBook'][self.id]
