from django.db import models
from users.models import User
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Invoice(models.Model):
	STATUS_CHOICES = (
		('Pending', 'Pending'),
		('Paid', 'Paid'),
		('Cancelled', 'Cancelled'),
	)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,related_name="invoice_customer")
	description = models.TextField(max_length=200,null=True, blank=True)
	price = models.FloatField(null=True)
	status = models.CharField(choices = STATUS_CHOICES,default='Pending',max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	items = models.ManyToManyField('Item',null=True,blank=True,related_name="invoice_items")

	def __str__(self):
		return self.customer.email

class Item(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
	product_name = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.product_name