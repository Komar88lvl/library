from django.db import transaction
from rest_framework import serializers

from book.models import Book
from borrowing.models import Borrowing
from book.serializers import BookSerializer


class BorrowingListSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "actual_return_date",
            "user",
            "book",
        )


class BorrowingRetrieveSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "user",
            "book",
        )


class BorrowingCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "book",
            "expected_return_date",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        book = attrs["book"]

        if book.inventory <= 0:
            raise serializers.ValidationError(
                "This book is not available now"
            )
        return attrs

    def create(self, validated_data):
        book = validated_data["book"]
        with transaction.atomic():
            book.inventory -= 1
            book.save()
            borrowing = Borrowing.objects.create(**validated_data)
        return borrowing
