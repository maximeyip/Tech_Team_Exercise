from django.db import models
from Tech_Team import settings

class Product(models.Model):
	product_id = models.IntegerField(unique=True)
	product_name = models.CharField(max_length=255)
	inventory_level = models.IntegerField()
	date = models.DateField(auto_now=False, auto_now_add=False)
	test = models.CharField(max_length=255)

# Create your models here.
