
from django.test import TestCase
from .models import Book
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import *


class StoreViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="harsh",
            email="test@email.com",
            password="password"
        )
       # author = Author.objects.create(first_name="Stephen", last_name="King")
        book = Book.objects.create(title="Cujo", authors='harsh', price=9)

    

    def test_cart(self):
        resp = self.client.get('/cart/')
        self.assertEqual(resp.status_code, 302)

    # testing for add to cart
    def test_add_to_cart(self):
        self.logged_in = self.client.login(username="harsh", password="password")
        self.assertTrue(self.logged_in)
        resp = self.client.get('/add/1/')
        resp = self.client.get('/cart/')
        self.assertEqual(resp.context['total'], int('9'))
        self.assertEqual(resp.context['count'], 1)
        self.assertEqual(resp.context['cart'].count(), 1)
        self.assertEqual(resp.context['cart'].get().quantity, 1)

     #testing for remove cart
    def test_remove_to_cart(self):
        self.logged_in = self.client.login(username="harsh", password="password")
        self.assertTrue(self.logged_in)
        resp = self.client.get('/remove/1/')
        resp = self.client.get('/cart/')
        self.assertEqual(resp.context['total'], int('0'))
        self.assertEqual(resp.context['count'], 0)
        