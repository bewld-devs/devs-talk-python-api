from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class FeedsSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Feed
        fields = '__all__'