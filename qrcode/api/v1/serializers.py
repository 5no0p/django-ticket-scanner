from rest_framework import serializers
from qrcode.models import QrcodeGenerator
from ticket.models import Ticket
from ticket.api.v1.serializers import CategoryTicketSerializer

class TicketQRcodeSerializer(serializers.ModelSerializer):
    category = CategoryTicketSerializer()
    class Meta:
        model = Ticket
        fields = ['uuid', 'name', 'validity', "table" ,'category']

class QrcodeGeneratorSerializer(serializers.ModelSerializer):
    ticket = TicketQRcodeSerializer()
    class Meta:
        model = QrcodeGenerator
        fields = ['id','uuid', 'ticket', 'qrcode']