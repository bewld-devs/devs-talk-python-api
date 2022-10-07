from django.urls import path
from .views import *

urlpatterns = [
    path('feeds', FeedsClass.as_view({'get': 'list'})),
    path('feeds/<int:pk>', FeedsClass.as_view({'get': 'retrieve'})),
    path('feeds/create', FeedsClass.as_view({'post': 'create'})),
    path('feeds/update/<int:pk>', FeedsClass.as_view({'patch': 'update'})),
    path('feeds/delete/<int:pk>', FeedsClass.as_view({'delete': 'destroy'})),
]