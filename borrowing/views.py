from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from borrowing.models import Borrowing
from borrowing.serializers import BorrowingSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = ()
