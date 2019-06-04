from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings

from likes.models import Like


# Create your models here.
class TopHeadline(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    urlToImage = models.CharField(max_length=200)
    publishedAt = models.DateTimeField()
    likes = GenericRelation(Like)
    views = models.IntegerField(default=0)
    favourites = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
