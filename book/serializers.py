from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "title", "author", "cover", "inventory", "daily_fee")
