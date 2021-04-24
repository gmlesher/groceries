from django.db import models
from django.contrib.auth.models import User 
from datetime import date

from .choices import *
        

class GroceryItem(models.Model):
    """An item the user has or would like to buy"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY, default="USD")
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    brand = models.CharField(max_length=50, blank=True)
    unit_of_measurement = models.CharField(max_length=8, choices=UNIT_OF_MEASUREMENT, blank=True)
    sku_size = models.FloatField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    mfg_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['name'] 

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class GroceryList(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(GroceryItem, related_name="GroceryList_Items_QuerySet")

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
