from django.urls import path
from .views import *

urlpatterns = [
    path('comments', CommentsClass.as_view({'get': 'list'})),
    path('comments/<int:pk>', CommentsClass.as_view({'get': 'retrieve'})),
    path('comments/create', CommentsClass.as_view({'post': 'create'})),
    path('comments/update/<int:pk>', CommentsClass.as_view({'patch': 'update'})),
    path('comments/delete/<int:pk>', CommentsClass.as_view({'delete': 'destroy'})),
]