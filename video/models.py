from django.db import models
from embed_video.fields import EmbedVideoField
from django.db.models.fields import AutoField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class CategoryList(models.Model):
    name=models.TextField(max_length=50,unique=True)
    img=models.ImageField(upload_to='categorylist',blank=True)
    slug=models.SlugField(unique=True,max_length=100)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name



class Item(models.Model):
    sno=models.AutoField(primary_key=True)
    category=models.ForeignKey(CategoryList,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='videosimages',blank=True)
    slug=models.SlugField(unique=True)
    title=models.CharField(max_length=200)
    video=EmbedVideoField()
    desc=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=('title',)

    def __str__(self):
        return self.title    


class VideoComment(models.Model):
    srno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    article=models.ForeignKey(Item,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.comment[0:10] + "..." + "by " + self.user.username



