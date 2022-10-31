from wsgiref import validate
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class EducationSerializer(serializers.ModelSerializer):
    many=True   
    
    class Meta:
        model = Education
        
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    many=True   
    
    class Meta:
        model = Work
        
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    # user = CustomUserSerializer
    education = EducationSerializer
    work = WorkSerializer  
    
    class Meta:
        model = Profile
        exclude = ["user"]

class CustomUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomUserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        instance.save()
        return instance
    
    # def update(self, instance, validated_data):
    #     user = self.context['request'].user
        
    #     if user.pk != instance.pk:
    #         raise serializers.ValidationError({"authorize": "You don't have permission to update this user"})

    #     instance.password = validated_data['password']
    #     instance.save()

    #     return instance
    
    class Meta:
        model = CustomUser
        exclude = ("last_login", "is_superuser", "is_staff", "is_active", "user_permissions", "groups")







