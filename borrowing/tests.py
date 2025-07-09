from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from datetime import date

from book.models import Book
from borrowing.models import Borrowing

BORROWING_URL = reverse("borrowing:borrowing-list")


class UnauthenticatedBorrowingTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(BORROWING_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedBorrowingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.test",
            password="testpassword",
        )
        self.client.force_authenticate(self.user)

    def test_create_borrowing(self):
        book = Book.objects.create(
            title="test title",
            author="test author",
            cover="HARD",
            inventory=5,
            daily_fee=0.5,
        )

        payload = {
            "book": book.id,
            "expected_return_date": date(2026, 5, 15)
        }

        res = self.client.post(BORROWING_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Borrowing.objects.count(), 1)

        borrowing = Borrowing.objects.first()

        self.assertEqual(borrowing.user, self.user)
        self.assertEqual(borrowing.book, book)
        self.assertEqual(str(borrowing.expected_return_date), "2026-05-15")
