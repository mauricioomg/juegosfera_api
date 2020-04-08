from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.api.serializers import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework import viewsets
from . import serializers
from . import models

from django.contrib.auth.models import User

class Product1Viewset(viewsets.ModelViewSet):
    queryset = models.Product1.objects.all()
    serializer_class = serializers.Product1Serializer

#list(), retrieve(), create(), update(), destroy()    


class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
   queryset = User.objects.all().order_by('-date_joined')
   serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_class = (TokenAuthentication)