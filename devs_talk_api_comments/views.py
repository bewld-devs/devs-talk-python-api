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
    queryset = Comment.objects.all()

    
    def list(self, request, pk=None):
        comments = Comment.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response({"status": "success", "results": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if pk:
            comment = Comment.objects.get(id=pk)
            serializer = CommentsSerializer(comment)
            return Response({"status": "success", "result": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        new_comment = CommentsSerializer(data=request.data)
        if new_comment.is_valid():
            new_comment.save()
            return Response({"status": "success", "result": new_comment.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": new_comment.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    def update(self, request, pk=None):
        update_comment = Comment.objects.get(id=pk)
        serializer = CommentsSerializer(update_comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "updated", "result": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def destroy(self, request, pk=None):
        delete_comment = get_object_or_404(Comment, id=pk)
        delete_comment.delete()
        return Response({"status": "success", "data":"Comment deleted!"}, status=status.HTTP_200_OK)
           


class RepliesClass(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    ):

    serializer_class = RepliesSerializer
    queryset = Reply.objects.all()

    
    def list(self, request, pk=None):
        replies = Reply.objects.all()
        serializer = RepliesSerializer(replies, many=True)
        return Response({"status": "success", "results": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        if pk:
            reply = Reply.objects.get(id=pk)
            serializer = RepliesSerializer(reply)
            return Response({"status": "success", "result": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        new_reply = RepliesSerializer(data=request.data)
        if new_reply.is_valid():
            new_reply.save()
            return Response({"status": "success", "result": new_reply.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": new_reply.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    def update(self, request, pk=None):
        update_reply = Reply.objects.get(id=pk)
        serializer = RepliesSerializer(update_reply, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "updated", "result": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "result": serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def destroy(self, request, pk=None):
        delete_reply = get_object_or_404(Reply, id=pk)
        delete_reply.delete()
        return Response({"status": "success", "data":"Comment deleted!"}, status=status.HTTP_200_OK)

