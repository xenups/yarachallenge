from django.conf import settings
from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Movies(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(unique=True)
    books = models.ManyToManyField(Books, verbose_name="books")
    movies = models.ManyToManyField(Movies, verbose_name="movies")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug
