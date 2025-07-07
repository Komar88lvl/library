from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

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
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "retrieve":
            return BorrowingRetrieveSerializer
        if self.action == "create":
            return BorrowingCreateSerializer

        return BorrowingListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
