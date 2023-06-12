from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        responce = self.client.get(reverse('index-page'))
        exp_data = 'Main Page'
        self.assertEqual(exp_data, responce.content.decode())
        self.assertEqual(200, responce.status_code)

    def test_test_page(self):
        responce = self.client.get(reverse('test_page'))
        exp_data = 'Test'
        self.assertEqual(exp_data, responce.content.decode())
        self.assertEqual(404, responce.status_code)

    def test_get_contacts(self):
        responce = self.client.get(reverse('contacts_page'))
        exp_data = 'Это контакты'
        self.assertEqual(exp_data, responce.content.decode())
        self.assertEqual(200, responce.status_code)

    def test_get_about(self):
        responce = self.client.get(reverse('about_page'))
        exp_data = 'Это страница about'
        self.assertEqual(exp_data, responce.content.decode())
        self.assertEqual(200, responce.status_code)