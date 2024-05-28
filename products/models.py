from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name_uz = models.CharField(max_length=20000, null=True)
    name_en = models.CharField(max_length=20000, null=True)
    name_ru = models.CharField(max_length=20000, null=True)
    image = models.ImageField(upload_to='Categoryimg', null=True)

    def __str__(self):
        return self.name_uz


class Banner(models.Model):
    theme_uz = models.CharField(max_length=10000, null=True)
    theme_en = models.CharField(max_length=10000, null=True)
    theme_ru = models.CharField(max_length=10000, null=True)
    image = models.ImageField(upload_to="Bannerpic", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.theme_uz


class Fotogallery(models.Model):
    name = models.CharField(max_length=9000, null=True)
    image = models.ImageField(upload_to='Fotogalleryimg', null=True, blank=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name_uz = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name_uz


class Products(models.Model):
    title_uz = models.CharField(max_length=20000, null=True)
    title_en = models.CharField(max_length=20000, null=True)
    title_ru = models.CharField(max_length=20000, null=True)
    description_uz = models.TextField(null=True)
    description_en = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='Productimg', null=True)

    def __str__(self):
        return self.title_uz