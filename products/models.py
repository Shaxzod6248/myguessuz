from django.db import models
from rest_framework import permissions
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name_uz = models.CharField(max_length=20000)
    name_ru = models.CharField(max_length=20000)

    def __str__(self):
        return self.name_uz


class Color(models.Model):
    name_uz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)

    def __str__(self):
        return self.name_uz


class Banner(models.Model):
    theme_uz = models.CharField(max_length=10000)
    theme_ru = models.CharField(max_length=10000)
    image = models.ImageField(upload_to="Aboutuspic")

    def __str__(self):
        return self.theme_uz


class Products(models.Model):
    image = models.ImageField(upload_to='products_image')
    title_uz = models.CharField(max_length=20000)
    title_ru = models.CharField(max_length=20000)
    description_uz = models.TextField()
    description_ru = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title_uz