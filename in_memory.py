class DB:
    ebooks = {}
    objects = {}

    def get(attr, id):
        return objects.get(attr, {}).get(id, None)

    def insert(attr, item):
        try:
            items = DB.objects[attr]
        except KeyError:
            print('There is no such object in DB!')
            DB.objects[attr] = {}
            items = DB.objects[attr]

        try:
            items[item.id] = item
        except AttributeError:
            raise Exception('Item in DB is not valid!')
        return True