from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from rest_framework import viewsets, permissions
from apps.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import generics
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
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication)

#class LoginViewset(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    form_class = AuthenticationForm
#    
#
#    @method_decorator(csrf_protect)
#   
#    def dispatch(self, request, *args, **kwargs):
#        if request.user.is_authenticated:
#            print("me autentique")
#        else:
#            return super(Login, self).dispatch(request, *args, **kwargs)
#
#    def form_valid(self, form):
#        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#        token,_ = Token.objects.get_or_create(user = user)
#        if token:
#            login(self.request, form.get_user())
#            return super(Login, self).form_valid(form)    
#    
#
#

