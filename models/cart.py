from in_memory import DB


class Cart:

    def __init__(self, session_id):
        self.id = session_id
        self.products_list = []
        self._insert()

    def _insert(self):
        if not DB.objects.get('Cart', None):
            DB.objects['Cart'] = {}
        DB.objects['Cart'][self.id] = self

    @staticmethod
    def get(id):
        if DB.objects.get('Cart', {}):
            return DB.objects.get('Cart', {}).get(id, None)

    @staticmethod
    def get_all():
        return DB.objects.get('Cart', {})

    def update_state(self):
        pass

    def remove(self):
        try:
            del DB.objects['Cart'][self.id]
        except (KeyError, AttributeError):
            raise Exception("There is no such object in DB")