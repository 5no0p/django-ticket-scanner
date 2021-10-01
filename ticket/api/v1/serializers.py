from django.db.models import fields
from rest_framework import serializers
from ticket.models import Ticket,Category,ScanLogs
from payment.models import Payment
from users.models import User
from event.models import Event
#from qrcode.models import QrcodeGenerator

class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','phoneNumber']

class UserScanLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','phoneNumber']

class EventGategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['uuid', 'name']
class CategoryTicketSerializer(serializers.ModelSerializer):
    event = EventGategorySerializer()
    class Meta:
        model = Category
        fields = ['name','event']

class TicketCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['uuid','name', 'validity']

class TicketScanLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['uuid','name', 'validity']

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['uuid','name', 'active_in']

class PaymentTicketSerializer(serializers.ModelSerializer):
    purchased_by = UserPaymentSerializer()
    class Meta:
        model = Payment
        #fields = ['uuid', 'purchased_by','amount_of_payment','status','purchased_at','screenshot']
        exclude = ['id','ticket']

# class QrcodeTicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= QrcodeGenerator
#         fields= ['uuid', 'qrcode']

class TicketSerializer(serializers.ModelSerializer):
    payment_info = PaymentTicketSerializer()
    category = CategoryTicketSerializer()
    #ticket_qrcode = QrcodeTicketSerializer(many=True)
    class Meta:
        model = Ticket
        fields = ['uuid', 'name', 'category', 'validity', "payment_info",'table','qrcode']

class CategorySerializer(serializers.ModelSerializer):
    event = EventCategorySerializer()
    tickets = TicketCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['name', 'price', 'discripton', 'event','tickets']

class ScanLogsSerializer(serializers.ModelSerializer):
    scanned_by = UserScanLogsSerializer()
    ticket = TicketScanLogsSerializer()
    class Meta:
        model = ScanLogs
        fields = ['ticket', 'scan_time', 'scanned_by', 'status_recorded']