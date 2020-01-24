import uuid
from in_memory import DB


class EBook:

    def __init__(self, name, price, available, cover):
        self._id = uuid.uuid4
        self.name = name
        self.price = price
        self.available = available
        self.cover = cover

    def insert(self):
        if not DB.objects.get('EBook', None):
            DB.objects['EBook'] = {}
        DB.objects['EBook'][self._id] = self

    @staticmethod
    def get(_id):
        if DB.objects.get('EBook', {}):
            return DB.objects.get('EBook', {}).get(_id, None)

    def update_state(self):
        self.insert()

    def remove(self):
        try:
            del DB.objects['EBook'][self._id]
        except (KeyError, AttributeError):
            raise Exception("There is no such object in DB")
