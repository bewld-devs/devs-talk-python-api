from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from devs_talk_api_app.models import CustomUser
from devs_talk_api_feeds.models import Feed





class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=True, blank=True,)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    title = models.CharField(max_length=19, null=True, blank=True, unique=True)    
    # image = CloudinaryField('image', folder='devs-talk-python-api')
    comment = models.TextField(max_length=120, null=True, blank=True,)
    code_snippet = models.TextField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    popularity = models.IntegerField(default=0, null=True, blank=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Comment by {self.author}'

    
class LikedComment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.feed.title + " liked by " + self.user.username

class DislikedComment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.feed.title + " disliked by " + self.user.username

class ClappedComment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.feed.title + " clapped by " + self.user.username

