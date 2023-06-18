from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post

# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title="Test", content="Test")

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

    def test_get_post_detail(self):
        responce = self.client.get(reverse('post-detail', args=(self.post.pk, )))
        self.assertTemplateUsed(responce, 'blog/post_detail.html')
        self.assertEqual(200, responce.status_code)

    def test_post_update(self):
        responce = self.client.get(reverse('post-update', args=(1, )))
        self.assertTemplateUsed(responce, 'blog/post_update.html')
        self.assertEqual(200, responce.status_code)

    def test_post_delete(self):
        responce = self.client.get(reverse('post-delete', args=(1, )))
        self.assertTemplateUsed(responce, 'blog/post_delete.html')
        self.assertEqual(200, responce.status_code)