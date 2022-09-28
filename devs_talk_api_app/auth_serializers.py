from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomUserSerializer, self).create(validated_data)
    
    
    class Meta:
        model = CustomUser
        exclude = ("last_login", "is_superuser", "is_staff", "is_active", "user_permissions", "groups")