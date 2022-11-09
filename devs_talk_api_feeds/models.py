from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from devs_talk_api_app.models import CustomUser



LANGUAGE = (
    ('Vue','VUE'),
    ('Python','PYTHON'),
    ('Javascript','JAVASCRIPT'),
    ('Ruby','RUBY'),
    ('Java','JAVA'),
    ('Rails','RAILS'),
    ('React','REACT'),
    ('Angular','ANGULAR'),
    ('Php','PHP'),
    ('Laravel','Laravel'),
    ('Django','DJANGO'),
)


class Feed(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)    
    image = CloudinaryField('image', folder='devs-talk-python-api')
    language = models.CharField(choices=LANGUAGE, max_length=155, null=True, blank=True)
    description = models.TextField(max_length=520, null=True, blank=True)
    code_snippet = models.TextField(max_length=520, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    popularity = models.IntegerField(default=0, null=True, blank=True)
    is_solved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    
class LikedFeed(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.feed.title + " liked by " + self.user.username

class DislikedFeed(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.feed.title + " disliked by " + self.user.username

class ClappedFeed(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.feed.title + " clapped by " + self.user.username
