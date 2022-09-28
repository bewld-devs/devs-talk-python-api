from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('users', CustomUserClass.as_view()),
<<<<<<< HEAD
    
=======
    path('users/<int:pk>', CustomUserClass.as_view()),
>>>>>>> f544f69be8527b3d88793bc8b0f525ec49b92c73
]