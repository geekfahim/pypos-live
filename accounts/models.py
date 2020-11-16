from django.db import models

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=200)
	phone=models.CharField(max_length=200,null=True,unique=True)
	email=models.CharField(max_length=200,null=True)
	address=models.CharField(max_length=200,null=True)
	create_date=models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name=models.CharField(max_length=200,null=True,unique=True)

	def __str__(self):
		return self.name
class Category(models.Model):
	name = models.CharField(max_length=200,null=True,unique=True)
	status = models.BooleanField(default=True)
	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=200,null=True,unique=True)
	def __str__(self):
		return self.name

class Product(models.Model):
	# CATEGORIES=(
	# 	('grocery','grocery'),
	# 	('medical','medical'),
	# 	('dailyneeds','dailyneeds')
	# 	)
	PARAMETER=(
		('kg','kg'),
		('piece','piece'),
		('ltr','ltr')
		)
	name=models.CharField(max_length=200)
	purchase_price=models.FloatField(max_length=200,null=True)
	selling_price=models.FloatField(max_length=200,null=True)
	quantity=models.IntegerField(null=True)
	barcode=models.CharField(max_length=200,blank=True)
	total_quantity=models.IntegerField(default=0)
	perameter=models.CharField(max_length=200,choices=PARAMETER,null=True)
	category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
	brand=models.ForeignKey(Brand,null=True,on_delete=models.SET_NULL)
	description=models.CharField(max_length=200)
	tag=models.ManyToManyField(Tag)
	create_date=models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS=(
		('paid','paid'),
		('due','due'),
		('cancel','cancel')
		)
	customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
	product=models.ManyToManyField(Product)
	discount=models.FloatField(max_length=200,null=True)
	total=models.FloatField(max_length=200,null=True)
	paid=models.FloatField(max_length=200,null=True)
	due=models.FloatField(max_length=200,null=True)
	status=models.CharField(max_length=200,choices=STATUS)
	create_date=models.DateTimeField(auto_now_add=True,null=True)
	

	def __str__(self):
		return self.product.name


class Expense(models.Model):
	name=models.CharField(max_length=200)
	amount=models.IntegerField(null=False,default=0)
	create_date=models.DateTimeField(auto_now_add=True,null=True)

class AppConfig(models.Model):
	app_name=models.CharField(max_length=200,default='pypos',null=True,unique=True)
	phone=models.CharField(max_length=200,default="01303351768",null=True)
	address=models.CharField(max_length=200,default='Dhaka,Bangladesh',null=True)
	currency=models.CharField(max_length=200,default='৳',null=True)
	invoice_terms=models.CharField(max_length=200,null=True)