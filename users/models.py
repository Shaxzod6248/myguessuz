from django.db import models
from django.contrib.auth.models import User


class Aboutus(models.Model):
    title_uz = models.CharField(max_length=10000)
    title_ru = models.CharField(max_length=10000)
    text_uz = models.TextField()
    text_ru = models.TextField()

    def __str__(self):
        return self.theme_uz


class Review(models.Model):
    comment_uz = models.TextField()
    comment_ru = models.TextField()

    def __str__(self):
        return self.comment_uz