from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from borrowing.notifications.telegram import send_telegram_notifications

from borrowing.models import Borrowing
from borrowing.serializers import (
    BorrowingListSerializer,
    BorrowingRetrieveSerializer,
    BorrowingCreateSerializer
)


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingListSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "retrieve":
            return BorrowingRetrieveSerializer
        if self.action == "create":
            return BorrowingCreateSerializer

        return BorrowingListSerializer

    def perform_create(self, serializer):
        borrowing = serializer.save(user=self.request.user)

        message = (
            f"New Borrowing Created\n"
            f"Book: {borrowing.book.title}\n"
            f"User: {borrowing.user.first_name} {borrowing.user.last_name}\n"
            f"Borrowed on: {borrowing.borrow_date}\n"
            f"Expected return: {borrowing.expected_return_date}"
        )

        try:
            send_telegram_notifications(message)
        except Exception as e:
            print(f"Fail to send telegram message: {e}")
