from rest_framework import serializers
from products.models import Category, Products, Banner
from users.models import Aboutus, Review, User
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        depth = 1
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class AboutusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'