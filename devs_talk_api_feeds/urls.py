from django.urls import path
from .views import *

urlpatterns = [
    path('feeds', FeedsClass.as_view()),
    path('feeds/<int:pk>', FeedsClass.as_view()),
]