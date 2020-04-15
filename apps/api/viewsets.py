from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from apps.api.serializers import UserSerializer
from django.contrib.auth.models import User
from . import serializers
from . import models


class Product1Viewset(viewsets.ModelViewSet):
    queryset = models.Product1.objects.all()
    serializer_class = serializers.Product1Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication)

#list(), retrieve(), create(), update(), destroy()    


class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication)


