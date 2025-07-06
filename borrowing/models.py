from django.db import models

from book.models import Book
from user.models import User


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name="borrowings"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="borrowings"
    )

    class Meta:
        ordering = ["-borrow_date"]

    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name} "
                f"borrowed {self.book.title} on {self.borrow_date}")
