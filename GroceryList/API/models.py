from django.db import models
from django.contrib.auth.models import User
from django_fsm import FSMField, transition

#


class GroceryItem(models.Model):
    UOM = (
        ('ml','ml'),
        ('L','L'),
        ('gm','gm'),
        ('kg', 'kg'),
        ('fl','fl'),
        ('oz','oz'),
        ('lb','lb')
    )
    CURRENCY = (
        ('INR', 'INR'),
        ('USD','USD')
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    unit_of_measurement = FSMField(default = 'gm', choices=UOM)
    sku_size = models.PositiveIntegerField()
    brand = models.CharField(max_length=50)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = FSMField(default = 'INR', choices=CURRENCY)

class GroceryList (models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(GroceryItem, related_name='GroceryList_Items_QuerySet')