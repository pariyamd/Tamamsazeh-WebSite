from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    pdf = models.FileField(blank=True, null=True, upload_to="articles/")

    class Meta:
        abstract = True


class Article(Blog):
    author = models.CharField(max_length=100, blank=True, default='unknown', null=True)


class Post(Blog):
    text = models.CharField(max_length=100000, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
