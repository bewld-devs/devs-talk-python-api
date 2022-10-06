from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .feed_serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets


class FeedsClass(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,):
    
    def list(self, request, pk=None):
        feeds = Feed.objects.all()
        serializer = FeedsSerializer(feeds, many=True)
        return Response({"status": "success", "results": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if pk:
            feed = Feed.objects.get(id=pk)
            serializer = FeedsSerializer(feed)
            return Response({"status": "success", "result": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        new_feed = FeedsSerializer(data=request.data)
        if new_feed.is_valid():
            new_feed.save()
            return Response({"status": "success", "result": new_feed.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": new_feed.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    def update(self, request, pk=None):
        update_feed = Feed.objects.get(id=pk)
        serializer = FeedsSerializer(update_feed, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "updated", "result": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def destroy(self, request, pk=None):
        delete_feed = get_object_or_404(Feed, id=pk)
        delete_feed.delete()
        return Response({"status": "success", "data":"Feed deleted!"}, status=status.HTTP_200_OK)
           

