from rest_framework import serializers
from event.models import Event
from ticket.api.v1.serializers import UserPaymentSerializer


class EventSerializer(serializers.ModelSerializer):
    owner = UserPaymentSerializer()
    class Meta:
        model = Event
        fields = ['uuid', 'name', 'active_in', 'discripton', 'owner']
        