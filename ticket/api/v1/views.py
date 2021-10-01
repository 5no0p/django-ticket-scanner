from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from ticket.api.v1.serializers import TicketSerializer,CategorySerializer,ScanLogsSerializer
from ticket.models import Ticket,Category,ScanLogs

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category','validity']
    search_fields = ['uuid', 'category__event', 'name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ScanLogsViewSet(viewsets.ModelViewSet):
    queryset = ScanLogs.objects.all()#.order_by('-scan_time')
    serializer_class = ScanLogsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering = ['-scan_time']