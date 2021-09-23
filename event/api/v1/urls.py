from django.urls import include, path
from rest_framework import routers
from event.api.v1 import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
]