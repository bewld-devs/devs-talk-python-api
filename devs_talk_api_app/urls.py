from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('users', CustomUserClass.as_view()),
    path('api/resistration', CustomUserClass.as_view()),
    path('users/<int:pk>', CustomUserClass.as_view()),
]