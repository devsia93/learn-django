from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from mysite.models import *

# Create your tests here.


class ApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user@foo.com', email='user@foo.com', password='top_secret')
        self.client = APIClient()
        t1 = Toping.objects.create(
            title='test1', content='test1', slug='test-one')
        t2 = Toping.objects.create(
            title='test2', content='test2', slug='test-two')
        p1 = Pizza.objects.create(
            title='Тест pizza one 1', content='test pizza one', cook=self.user)
        p1.topings.set([t1, t2])
        p2 = Pizza.objects.create(
            title='Тестовая 211235 two что-то!,.; там', content='test post two', cook=self.user)

    def test_get_pizzes(self):
        response = self.client.get('/api/pizzes/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_post_pizza(self):
        response = self.client.post(
            '/api/pizzes/', data={'title': 'test new pizza', 'content': 'test content', 'cook': self.user})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Pizza.objects.all()), 3)
