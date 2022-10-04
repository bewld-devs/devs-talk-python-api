import uuid
from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from devs_talk_api_app.models import CustomUser



LANGUAGE = (
    ('Html','HTML'),
    ('Python','PYTHON'),
    ('Javascript','JAVASCRIPT'),
    ('Ruby','RUBY'),
)


class Feed(models.Model):
    # id = uuid.UUIDField(primary_key=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    title = models.CharField(max_length=19, null=True, blank=True, unique=True)    
    # image = CloudinaryField('image', folder='devs-talk-python-api')
    image = models.FileField(max_length=400, null=True, blank=True)
    language = models.CharField(choices=LANGUAGE, max_length=55, null=True, blank=True)
    content = models.TextField(max_length=120, null=True)
    created_at = models.BooleanField(default=False)
    updated_at = models.BooleanField(default=False)
    popularity = models.IntegerField(default=0, null=True, blank=True)
    is_solved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    

