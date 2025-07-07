from rest_framework import serializers

from borrowing.models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(read_only=True, many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user"
        )
