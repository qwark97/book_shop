from django.db import models


class EBook(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField()
    cover = models.FilePathField()
