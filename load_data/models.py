from django.db import models

class Stock(models.Model):
	cod_local = models.CharField(max_length=150)
	cod_mat = models.IntegerField()
	instock = models.IntegerField() 
	description = models.CharField(max_length=150)
	id_stock = models.IntegerField(unique=True) 

	def __unicode__(self):
		return self.description

# Create your models here.
