from django.urls import include, path
from rest_framework import routers
from ticket.api.v1 import views

router = routers.DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'scanlogs', views.ScanLogsViewSet)
router.register(r'qrcodes', views.QrcodeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]