from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        responce = self.client.get(reverse('index-page'))
        self.assertTemplateUsed(responce, 'blog/index.html')
        self.assertEqual(200, responce.status_code)

    def test_get_contacts(self):
        responce = self.client.get(reverse('contacts_page'))
        self.assertTemplateUsed(responce, 'blog/contacts.html')
        self.assertEqual(200, responce.status_code)

    def test_get_about(self):
        responce = self.client.get(reverse('about_page'))
        self.assertTemplateUsed(responce, 'blog/about.html')
        self.assertEqual(200, responce.status_code)