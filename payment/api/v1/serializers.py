from rest_framework import serializers
from payment.models import Payment
from ticket.models import Ticket
from ticket.api.v1.serializers import CategoryTicketSerializer,UserPaymentSerializer

class TicketPaymentSerializer(serializers.ModelSerializer):
    categeory = CategoryTicketSerializer
    class Meta:
        model = Ticket
        fields = ['uuid','name', 'category', 'extral_info']

class PaymentSerializer(serializers.ModelSerializer):
    ticket = TicketPaymentSerializer()
    purchased_by = UserPaymentSerializer()
    class Meta:
        model = Payment
        fields = ['uuid', 'purchased_by','amount_of_payment', 'ticket', 'status', 'purchased_at', 'screenshot'] 