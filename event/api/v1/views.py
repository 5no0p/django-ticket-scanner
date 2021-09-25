from rest_framework import viewsets
from rest_framework import permissions
from event.api.v1.serializers import EventSerializer
from event.models import Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'uuid'
    