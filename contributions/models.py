from django.db import models

class media(models.Model):
	id = models.CharField(max_length=10,primary_key=True)
	album= models.CharField(max_length=255)
	category= models.CharField(max_length=255)
	price= models.DecimalField(max_digits=10,decimal_places=2)
	singer= models.CharField(max_length=255)
	lyricist= models.CharField(max_length=255)
	musician= models.CharField(max_length=255)
	url= models.CharField(max_length=500)
	
class book(models.Model):
	id = models.CharField(max_length=10,primary_key=True)
	name= models.CharField(max_length=255)
	category= models.CharField(max_length=255)
	price= models.DecimalField(max_digits=10,decimal_places=2)
	author= models.CharField(max_length=255)
	url= models.CharField(max_length=500)
	
class customer(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255,primary_key=True)
	country_code = models.PositiveSmallIntegerField(default=91)
	mobile_number = models.PositiveIntegerField()
	landline_number = models.PositiveIntegerField()
	address1 = models.CharField(max_length=255)
	address2 = models.CharField(max_length=255)
	address3 = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	
class order(models.Model):
	order_no = models.PositiveIntegerField(primary_key=True)
	customer_email = models.ForeignKey(customer)
	order_date = models.DateTimeField()
	item_id = models.CharField(max_length=10)
	quantity = models.PositiveSmallIntegerField()
