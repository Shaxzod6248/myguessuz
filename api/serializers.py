from rest_framework import serializers
from products.models import Category, Products, Banner, Fotogallery, Subcategory
from users.models import Aboutus, Review


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        depth = 1
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AboutusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class FotogallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotogallery
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'