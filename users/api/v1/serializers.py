from rest_framework import serializers
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from ticket.models import SecurityLayer

User = get_user_model()

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ['app_label', 'model']
class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer()
    class Meta:
        model = Permission
        fields = ['name', 'codename', 'content_type']
class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ['name', 'permissions']
class UserSerializer(serializers.ModelSerializer):
    class UserSecuritySerializer(serializers.RelatedField):
        def to_representation(self, value):
            return value.layer

    groups = GroupSerializer(many=True)
    security = UserSecuritySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'user_permissions', 
            'groups',
            'is_superuser',
            'security'
            ]
        #exclude = ['password']