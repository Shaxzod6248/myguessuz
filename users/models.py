from django.db import models


class Aboutus(models.Model):
    title_uz = models.CharField(max_length=10000, null=True)
    title_en = models.CharField(max_length=10000, null=True)
    title_ru = models.CharField(max_length=10000, null=True)
    text_uz = models.TextField(null=True)
    text_en = models.TextField(null=True)
    text_ru = models.TextField(null=True)

    def __str__(self):
        return self.title_uz


class Review(models.Model):
    comment_uz = models.TextField(null=True)
    comment_en = models.TextField(null=True)
    comment_ru = models.TextField(null=True)

    def __str__(self):
        return self.comment_uz