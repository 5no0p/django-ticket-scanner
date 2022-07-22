
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('ticket.urls')),
    path('',include('event.urls')),
    path('',include('payment.urls')),
]
