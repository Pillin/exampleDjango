from django.test import TestCase
from load_data.views import processing_file
from load_data.models import Stock
# Create your tests here.
from django.core.files.base import ContentFile

class BaseTestUpload(TestCase):
    def setUp(self):
    	pass

    def tearDown(cls):
    	Stock.objects.all().delete()
    	pass


    def test_upload_file(self):
		myfile = open('load_data/test_file/prueba1.csv','r') 
		response = self.client.post('/load_data/csv/', data={'file': myfile})
		self.assertEqual(response.status_code, 200)
		list_stock = Stock.objects.all()
		self.assertEqual(list_stock.count(), 123)

		myfile = open('load_data/test_file/prueba1.csv','r') 
		response = self.client.post('/load_data/csv/', data={'file': myfile})
		self.assertEqual(response.status_code, 200)
		list_stock = Stock.objects.all()
		self.assertEqual(list_stock.count(), 123)

