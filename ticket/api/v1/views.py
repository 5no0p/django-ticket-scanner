from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from ticket.api.v1.serializers import TicketSerializer,CategorySerializer,ScanLogsSerializer
from ticket.models import Ticket,Category,ScanLogs
from users.models import User


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category','validity','qrcode']
    search_fields = ['qrcode','uuid']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'
    filter_backeds = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name','event']
    search_fields = ['event__uuid']


class ScanLogsViewSet(viewsets.ModelViewSet):
    queryset = ScanLogs.objects.all()#.order_by('-scan_time')
    serializer_class = ScanLogsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['status_recorded', 'scan_time', 'ticket']
    search_fields = ['scanned_by__username']
    ordering = ['-scan_time']

    def perform_create(self, serializer):
        ticket=self.request.data['ticket']
        ticket_instance, created = Ticket.objects.get_or_create(uuid=ticket)
        serializer.save(scanned_by=self.request.user,ticket=ticket_instance)
