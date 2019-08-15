from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Product(models.Model):

    class Meta:

        db_table = 'product'

    name = models.CharField(max_length=150)
    images = ArrayField(models.CharField(max_length=350, blank=True, default=""))
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.title