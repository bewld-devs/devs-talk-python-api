from modulefinder import packagePathMap
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
    return render(request, "index.html")

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


    def patch(self, request, pk=None):
        update_user = CustomUser.objects.get(id=pk)
        serializer = CustomUserSerializer(update_user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "result": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
           

    def delete(self, request, pk=None):
        delete_user = get_object_or_404(CustomUser, id=pk)
        delete_user.delete()
        return Response({"status": "success", "data":"Account deleted!"}, status=status.HTTP_200_OK)


class ProfileClass(APIView):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request, pk=None):
        if pk:
            profile = Profile.objects.get(id=pk)
            serializer = ProfileSerializer(profile)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 

    def post(self, request):
        new_profile = ProfileSerializer(data=request.data)
        if new_profile.is_valid():
            new_profile.save()
            return Response({"status": "success", "result": new_profile.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": new_profile.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    def patch(self, request, pk=None):
        update_profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(update_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "result": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
           

    def delete(self, request, pk=None):
        delete_profile = get_object_or_404(Profile, id=pk)
        delete_profile.delete()
        return Response({"status": "success", "data":"Profile deleted!"}, status=status.HTTP_200_OK)
