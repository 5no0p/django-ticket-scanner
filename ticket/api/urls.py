from django.urls import include, path

urlpatterns = [
    path('v1/', include('ticket.api.v1.urls')),
]