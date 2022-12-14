from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .auth_serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
# from .permissions import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


def index(request):
    return HttpResponse("Welcome to Devs Talk")

class CustomUserClass(APIView):
    
    def get(self, request, pk=None):
        if pk:
            user = CustomUser.objects.get(id=pk)
            serializer = CustomUserSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 

    def post(self, request):
        new_user = CustomUserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response({"status": "success", "result": new_user.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": new_user.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

