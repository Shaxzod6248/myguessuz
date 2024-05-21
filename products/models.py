from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Banner(models.Model):
    theme_uz = models.CharField(max_length=10000, null=True)
    theme_en = models.CharField(max_length=10000, null=True)
    theme_ru = models.CharField(max_length=10000, null=True)
    image = models.ImageField(upload_to="Bannerpic", null=True)

    def __str__(self):
        return self.theme_uz


class Category(models.Model):
    image = models.ImageField(upload_to='categoryimg', null=True)
    name_uz = models.CharField(max_length=20000, null=True)
    name_en = models.CharField(max_length=20000, null=True)
    name_ru = models.CharField(max_length=20000, null=True)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_uz


class Color(models.Model):
    name_uz = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name_uz


class Products(models.Model):
    image = models.ImageField(upload_to='products_image', null=True)
    title_uz = models.CharField(max_length=20000, null=True)
    title_en = models.CharField(max_length=20000, null=True)
    title_ru = models.CharField(max_length=20000, null=True)
    description_uz = models.TextField(null=True)
    description_en = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title_uz