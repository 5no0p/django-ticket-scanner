from django.urls import include, path

urlpatterns = [
    path('v1/', include('event.api.v1.urls')),
]