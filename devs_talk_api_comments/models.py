from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from devs_talk_api_app.models import CustomUser
from devs_talk_api_feeds.models import Feed





class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=True, blank=True,)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)   
    image = CloudinaryField('image', folder='devs-talk-python-api', null=True, blank=True)
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

#Replies

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True,)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)   
    image = CloudinaryField('image', folder='devs-talk-python-api', null=True, blank=True)
    reply = models.TextField(max_length=120, null=True, blank=True)
    code_snippet = models.TextField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    popularity = models.IntegerField(default=0, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

        ordering = ('-created_at',)

    def __str__(self):
        return f'Reply by {self.author}'

    
class LikedReply(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE,)
    like = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Liked reply'
        verbose_name_plural = 'Liked replies'

    def __str__(self):
        return self.feed.title + " liked by " + self.user.username

class DislikedReply(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    dislikes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Disliked reply'
        verbose_name_plural = 'Disliked replies'

    def __str__(self):
        return self.feed.title + " disliked by " + self.user.username

class ClappedReply(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    claps = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Clapped reply'
        verbose_name_plural = 'Clapped replies'

    def __str__(self):
        return self.feed.title + " clapped by " + self.user.username
