from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    MEDICINES = 'Medicines'
    FOOD = 'Food'
    FURNITURE = 'Furniture'
    OTHER = 'Other'

class Product(models.Model):
    name = models.CharField(verbose_name= 'Product', null=False, blank=False, max_length=200)
    category = models.CharField(verbose_name='Product Category', max_length=100, choices=CategoryChoice.choices, default=CategoryChoice.OTHER)
    description = models.CharField(verbose_name='Description', max_length=1000, null=True, blank=True)
    image = models.CharField(null=True,blank=True,verbose_name='Image', max_length=500)


