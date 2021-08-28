from django.contrib import admin
from .models import CategoryList, Item, VideoComment
from embed_video.admin import AdminVideoMixin
# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(CategoryList)
admin.site.register(VideoComment)
admin.site.register(Item,MyModelAdmin)
