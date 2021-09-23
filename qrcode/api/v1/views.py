from rest_framework import viewsets
from rest_framework import permissions
from qrcode.api.v1.serializers import QRcodeGeneratorSerializer
from qrcode.models import QRcodeGenerator

class QRcodeGeneratorViewSet(viewsets.ModelViewSet):
    queryset = QRcodeGenerator.objects.all()
    serializer_class = QRcodeGeneratorSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]