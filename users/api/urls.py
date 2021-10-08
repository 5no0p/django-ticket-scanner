from django.urls import include, path

urlpatterns = [
    path('v1/auth/', include('rest_auth.urls')),
    path('v1/auth/registration/', include('rest_auth.registration.urls')),

    path('v1/', include('users.api.v1.urls')),
]