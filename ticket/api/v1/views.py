from rest_framework import viewsets
from rest_framework import permissions
from ticket.api.v1.serializers import TicketSerializer,CategorySerializer,ScanLogsSerializer
from ticket.models import Ticket,Category,ScanLogs

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ScanLogsViewSet(viewsets.ModelViewSet):
    queryset = ScanLogs.objects.all()
    serializer_class = ScanLogsSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]