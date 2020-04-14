from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework.authtoken import views
from rest_framework import routers, serializers, viewsets

from .router import router



app_name = 'api' 

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth')   
]