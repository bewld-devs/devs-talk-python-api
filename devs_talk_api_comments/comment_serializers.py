from rest_framework import serializers
from .models import *


class CommentsSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Comment
        fields = '__all__'