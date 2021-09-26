from django.urls import include, path
from rest_framework import routers
from qrcode.api.v1 import views

router = routers.DefaultRouter()
router.register(r'qrcodes', views.QrcodeGeneratorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]