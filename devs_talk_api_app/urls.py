from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('users', CustomUserClass.as_view()),
    path('users/<int:pk>', CustomUserClass.as_view()),
    path('profile', ProfileClass.as_view()),
    path('profile/<int:pk>', ProfileClass.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
