from django.urls import path
from .views import *

urlpatterns = [
    path('replies', RepliesClass.as_view({'get': 'list'})),
    path('replies/<int:pk>', RepliesClass.as_view({'get': 'retrieve'})),
    path('replies/create', RepliesClass.as_view({'post': 'create'})),
    path('replies/update/<int:pk>', RepliesClass.as_view({'patch': 'update'})),
    path('replies/delete/<int:pk>', RepliesClass.as_view({'delete': 'destroy'})),
    
    path('comments', CommentsClass.as_view({'get': 'list'})),
    path('comments/<int:pk>', CommentsClass.as_view({'get': 'retrieve'})),
    path('comments/create', CommentsClass.as_view({'post': 'create'})),
    path('comments/update/<int:pk>', CommentsClass.as_view({'patch': 'update'})),
    path('comments/delete/<int:pk>', CommentsClass.as_view({'delete': 'destroy'})),


]