from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    author=models.CharField(max_length=13)
    timestamp=models.DateTimeField(blank=True)
    likes=models.ManyToManyField(User, related_name='likes',blank=True)
    models.IntegerField

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + 'by' + '' + self.author




