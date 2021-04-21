from django.test import TestCase
from django.contrib.auth.models import User
#from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from django.urls import reverse

from .models import Book


class StoreViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="harsh",
            email="test@email.com",
            password="password"
        )
        #author = Book.objects.create(authors="Stephen")
        book = Book.objects.create(title="Cujo", authors='author', price=90 )


    
    def test_book_detail(self):
        resp = self.client.get('/detail/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['book'].pk, 1)
        self.assertEqual(resp.context['book'].title, "Cujo")
        resp = self.client.get('/detail/2/')
        self.assertEqual(resp.status_code, 404)

    