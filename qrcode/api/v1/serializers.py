from django.db import models
from django.db.models import fields
from rest_framework import serializers
from qrcode.models import QRcodeGenerator
from ticket.models import Ticket
from ticket.api.v1.serializers import CategoryTicketSerializer

class TicketQRcodeSerializer(serializers.ModelSerializer):
    category = CategoryTicketSerializer()
    class Meta:
        model = Ticket
        fields = ['uuid', 'name', 'validity', "extral_info" ,'category']

class QRcodeGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRcodeGenerator
        fields = ['uuid', 'ticket', 'qrcode', 'qrimage']