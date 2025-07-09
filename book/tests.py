from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from book.models import Book

BOOK_URL = reverse("book:book-list")


class UnauthenticateBookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(BOOK_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_book_forbidden(self):
        book = Book.objects.create(
            title="test title",
            author="test author",
            cover="HARD",
            inventory=5,
            daily_fee=0.5,
        )

        payload = {
            "book": book,
        }

        res = self.client.post(BOOK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
