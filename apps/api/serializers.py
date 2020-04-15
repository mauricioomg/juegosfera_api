from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product1


class Product1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = '__all__'

 
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0 :
            raise serializers.ValidationError('Este nombre de usuario ya existe, ingrese uno nuevo')
        else:
            return data 
 