from rest_framework import viewsets
from rest_framework import permissions
from payment.api.v1.serializers import PaymentSerializer
from payment.models import Payment

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]