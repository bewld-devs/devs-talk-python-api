from rest_framework import serializers
from .models import *


class CommentsSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Comment
        fields = '__all__'


class RepliesSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Reply
        fields = '__all__'