from django.contrib import admin
from .models import Category, Products, Color, Banner, Fotogallery, Subcategory


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Products)
admin.site.register(Color)
admin.site.register(Banner)
admin.site.register(Fotogallery)