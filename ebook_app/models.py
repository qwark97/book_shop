from django.db import models


class EBook(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField()
    cover = models.FilePathField()

    def __str__(self):
        return self.name

    def attributes(self):
        return {
            'name': str,
            'price': float,
            'available': bool,
            'cover': str,
        }
