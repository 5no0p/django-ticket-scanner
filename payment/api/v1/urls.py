from django.urls import include, path
from rest_framework import routers
from payment.api.v1 import views

router = routers.DefaultRouter()
router.register(r'payments', views.PaymentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]