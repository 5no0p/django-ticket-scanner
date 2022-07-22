from django.urls import include, path
from rest_framework import routers
from users.api.v1 import views

router = routers.DefaultRouter()
router.register(r'permissions', views.PermissionViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]