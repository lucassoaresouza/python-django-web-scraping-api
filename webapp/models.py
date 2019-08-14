from django.db import models

# Create your models here.

class Product(models.Model):

    class Meta:

        db_table = 'product'

    name = models.CharField(max_length=150)
    image = models.CharField(max_length=350)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.title