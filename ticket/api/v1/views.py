import secrets
import string

from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from ticket.api.v1.pagination import ScanLogsPagination, TicketPagination
from ticket.api.v1.serializers import TicketSerializer,CategorySerializer,ScanLogsSerializer
from ticket.models import Ticket,Category,ScanLogs
from users.models import User


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = TicketPagination
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'tid'
    # ordering = ['-isSend']
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category','validity', 'is_checked','phone', 'name']
    search_fields = ['=qrcode']

    @action(methods=['post'],detail=False, url_path='multi')
    def multi(self, request, pk=None):
        chars = string.ascii_letters + string.digits
        length = 30
        uiLenth = 13
        qrcode=''
        tid=''
        tickets_list=[]
        data = request.data
        number = int(data['id'])
        category = Category.objects.get_or_create(name=data['category'])
        for x in range(1, int(data['count'])+1):
            while True:
                qrcode = ''.join([secrets.choice(chars) for i in range(length)]) #range(length-1)
                #passwd += secrets.choice(special_chars)
                if (any(s.islower() for s in qrcode) and 
                    any(s.isupper() for s in qrcode) and 
                    any(s.isdigit() for s in qrcode)):
                        break
            
            tid = ''.join([secrets.choice(string.ascii_lowercase) for i in range(uiLenth-10)])
            tid += ''.join([secrets.choice(string.digits) for i in range(uiLenth-3)])
            tickets_list.append(Ticket(category=Category.objects.get(name=data['category']),
                                        number=number,
                                        qrcode=qrcode,
                                        tid=tid))
            number+= 1
        Ticket.objects.bulk_create(tickets_list)

        return Response(status.HTTP_201_CREATED)

class QrcodeViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'qrcode'
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['category','validity','qrcode']
    # search_fields = ['=qrcode']

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
    pagination_class = ScanLogsPagination
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['status_recorded', 'scan_time', 'ticket']
    search_fields = ['=scanned_by__username']
    ordering = ['-scan_time']

    def perform_create(self, serializer):
        ticket=self.request.data['ticket']
        ticket_instance, created = Ticket.objects.get_or_create(uuid=ticket)
        serializer.save(scanned_by=self.request.user,ticket=ticket_instance)
