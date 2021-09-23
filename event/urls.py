from django.urls import include, path

urlpatterns = [
    path('api/', include('event.api.urls')),
]