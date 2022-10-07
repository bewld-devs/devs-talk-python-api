from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Feed)
admin.site.register(DislikedFeed)
admin.site.register(LikedFeed)
admin.site.register(ClappedFeed)
