from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import Permission,Group
from users.api.v1.serializers import PermissionSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'name'
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name', 'codename', 'content_type']
    #search_fields = ['codename']