from django.db import models


# Create your models here.

class ProductModel(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)

    def __str__(self):
        return self.pname

    class Meta:
        db_table = 'productTable'


class ItemModel(models.Model):
    itemId = models.IntegerField(primary_key=True)
    itemName = models.CharField(max_length=100)
    pid = models.IntegerField()

    def __str__(self):
        return self.itemName

    class Meta:
        db_table = 'itemsTable'
