from django.test import TestCase
from .models import MagicItem
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)
    def test_product(self):
          amulet = MagicItem.objects.create(
          name= "Amulet of Rain Detection",
          type = "neck item",
          description = "This amulet allows its wearer to detect when its raining, not before, only during. It only works outdoors.",
          price = 0
          )
          self.assertTrue(amulet.is_not_a_waste_of_money)