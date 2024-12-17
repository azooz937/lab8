from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    edition = models.PositiveIntegerField()

    def __str__(self):
        return self.title
