from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class FeedsSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomUserSerializer, self).create(validated_data)
    
    
    class Meta:
        model = Feed
        fields = '__all__'