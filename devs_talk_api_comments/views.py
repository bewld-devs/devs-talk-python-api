# from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .comment_serializers import *
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets


class CommentsClass(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    ):

    serializer_class = CommentsSerializer
    
    def list(self, request, pk=None):
        comments = Comment.objects.all()
        serializer_class = CommentsSerializer(comments, many=True)
        return Response({"status": "success", "results": serializer_class.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if pk:
            comment = Comment.objects.get(id=pk)
            serializer_class = CommentsSerializer(comment)
            return Response({"status": "success", "result": serializer_class.data}, status=status.HTTP_200_OK)

    def create(self, request):
        new_comment = CommentsSerializer(data=request.data)
        if new_comment.is_valid():
            new_comment.save()
            return Response({"status": "success", "result": new_comment.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": new_comment.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    def update(self, request, pk=None):
        update_comment = Comment.objects.get(id=pk)
        serializer_class = CommentsSerializer(update_comment, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"status": "updated", "result": serializer_class.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": serializer_class.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def destroy(self, request, pk=None):
        delete_comment = get_object_or_404(Comment, id=pk)
        delete_comment.delete()
        return Response({"status": "success", "data":"Comment deleted!"}, status=status.HTTP_200_OK)
           


