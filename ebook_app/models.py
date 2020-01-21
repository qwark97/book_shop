from django.db import models


class EBook(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField()
    cover = models.FilePathField()

    def __str__(self):
        return 'Name: "%s" costs %d and is %savailable' % (
            self.name,
            self.price,
            '' if self.available else 'not '
        )

    def attributes(self):
        return {
            'name': str,
            'price': float,
            'available': bool,
            'cover': str,
        }
