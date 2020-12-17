from django.db import models
#from PIL import Image
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill

# Create your models here.

class product(models.Model):
	title=models.CharField(max_length=200)
	price=models.CharField(max_length=10)
	description=models.TextField()
	image=models.ImageField(upload_to='product_image',blank=True)
	s_id=models.ForeignKey('seller',on_delete=models.CASCADE)
	# stock=models.IntegerField()
	# category=models.IntegerField()
	class Meta:
		db_table="product"

class buyer(models.Model):
	b_email=models.CharField(max_length=100,primary_key=True)
	name=models.CharField(max_length=100)
	phno=models.CharField(max_length=20,null=True)
	class Meta:
		db_table="buyer"

class seller(models.Model):
	s_email=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=200)
	phno=models.CharField(max_length=20)
	class Meta:
		db_table="seller"

class cart(models.Model):
	bid=models.ForeignKey('buyer', on_delete=models.CASCADE,name='bid',null=False)
	pid=models.ForeignKey('product',	on_delete=models.CASCADE,name='pid')
	sid=models.ForeignKey('seller',on_delete=models.CASCADE,name='sid')
	quantity=models.IntegerField()
	price=models.IntegerField()
	class Meta:
		unique_together=(("pid","bid"),)
		db_table="cart"

class order(models.Model):
	bid=models.ForeignKey('buyer',on_delete=models.CASCADE,name='bid',null=False)
	pid=models.ForeignKey('product',on_delete=models.CASCADE,name='pid')
	sid=models.ForeignKey('seller',on_delete=models.CASCADE,name='sid')
	created_at = models.DateTimeField(auto_now_add=True)
	price=models.IntegerField()
	quantity=models.IntegerField()
	address=models.ForeignKey('address',on_delete=models.CASCADE)
	class Meta:
		unique_together=('bid','pid','sid','created_at')
		db_table="order1"

class address(models.Model):
	bid=models.ForeignKey('buyer',on_delete=models.CASCADE,name='bid',null=False)
	name=models.CharField(max_length=20)
	address=models.TextField()
	#ccnum=models.CharField(max_length=20)
	phno=models.CharField(max_length=20)
	class Meta:
		db_table="address"

