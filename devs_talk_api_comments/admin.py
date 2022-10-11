from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Comment)
admin.site.register(DislikedComment)
admin.site.register(LikedComment)
admin.site.register(ClappedComment)

admin.site.register(Reply)
admin.site.register(DislikedReply)
admin.site.register(LikedReply)
admin.site.register(ClappedReply)
