from django.test import TestCase, Client
from mysite.models import *
from django.contrib.auth.models import User


# Create your tests here.


class TopingTestCase(TestCase):
    # constants for equals
    toping_absolute_url_one = '/pizzes/toping/test-one/'
    toping_absolute_url_two = '/pizzes/toping/test-two/'

    toping_create_url = '/pizzes/toping/create/'
    # endconstants

    def setUp(self):
        t1 = Toping.objects.create(
            title='test1', content='test1', slug='test-one')
        t2 = Toping.objects.create(
            title='test2', content='test2', slug='test-two')

        user = User.objects.create_user(
            username='user@foo.com', email='user@foo.com', password='top_secret')
        self.client.login(username='user@foo.com', password='top_secret')

    def test_get_absolute_url(self):
        t1 = Toping.objects.get(pk=1)
        t2 = Toping.objects.get(pk=2)
        self.assertTrue(t1.get_absolute_url() == self.toping_absolute_url_one)
        self.assertTrue(t2.get_absolute_url() == self.toping_absolute_url_two)

    def test_toping_view(self):
        c = Client()
        response = c.get(self.toping_absolute_url_one)
        self.assertEqual(response.status_code, 200)

    def test_toping_post(self):
        c = Client()
        c.login(username='user@foo.com', password='top_secret')
        response = c.post(self.toping_create_url, {'title':'test-create', 'content':'test', 'slug': 'test'})
        self.assertEqual(response.status_code, 201)
