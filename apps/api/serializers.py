from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product1


class Product1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="index:user-detail")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if users.count() != 0 :
            raise serializers.ValidationError('Este nombre de usuario ya existe, ingrese uno nuevo')
        else:
            return data 

 
#class UserSerializer(serializers.Serializer):
 #   id = serializers.ReadOnlyField()
  #  first_name = serializers.CharField()
  #  last_name = serializers.CharField()
   # username = serializers.CharField()
    #email = serializers.EmailField()
    #assword = serializers.CharField()

    #def create(self, validate_data):
     #   instance = User()
      #  instance.first_name = validate_data.get('first_name')
       # instance.last_name = validate_data.get('last_name')
        #instance.username = validate_data.get('username')
        #instance.email = validate_data.get('email')
        #instance.set_password(validate_data.get('password'))
        #instance.save()
        #return instance

    #def validate_username(self, data):
    #    users = User.objects.filter(username = data)
    #    if len(users) != 0 :
    #        raise serializers.ValidationError('Este nombre de usuario ya existe, ingrese uno nuevo')
    #    else:
    #        return data 
 