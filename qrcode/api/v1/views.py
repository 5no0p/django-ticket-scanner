from rest_framework import viewsets
from rest_framework import permissions
from qrcode.api.v1.serializers import QrcodeGeneratorSerializer
from qrcode.models import QrcodeGenerator

class QrcodeGeneratorViewSet(viewsets.ModelViewSet):
    queryset = QrcodeGenerator.objects.all()
    serializer_class = QrcodeGeneratorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'qrcode'