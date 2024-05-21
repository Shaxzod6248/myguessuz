from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from products.models import Category, Banner, Products
from users.models import Aboutus, Review
from .serializers import (CategorySerializer, ProductsSerializer, BannerSerializer, AboutusSerializer, ReviewSerializer)
from rest_framework.response import Response


class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoriesDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategorySerializer(categories)
        return Response(serializer.data)

    def put(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategorySerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategorySerializer(categories, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        categories = self.get_object(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BannerAPIView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(
            banners, context={'request': request}, many=True)
        return Response(serializer.data)


class BannerDetail(APIView):
    def get_object(self, pk):
        try:
            return Banner.objects.get(id=pk)
        except Banner.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        banner = self.get_object(pk)
        serializer = BannerSerializer(banner)
        return Response(serializer.data)

    def put(self, request, pk):
        banner = self.get_object(pk)
        serializer = BannerSerializer(banner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        banner = self.get_object(pk)
        serializer = BannerSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        banner = self.get_object(pk)
        banner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsAPIView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AboutusAPIView(APIView):
    def get(self, request):
        aboutus = Aboutus.objects.all()
        serializer = AboutusSerializer(aboutus, many=True)
        return Response(serializer.data)


class AboutusDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        aboutus = self.get_object(pk)
        serializer = AboutusSerializer(aboutus)
        return Response(serializer.data)


    def put(self, request, pk):
        aboutus = self.get_object(pk)
        serializer = AboutusSerializer(aboutus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        aboutus = self.get_object(pk)
        serializer = AboutusSerializer(aboutus, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aboutus = self.get_object(pk)
        aboutus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewAPIView(APIView):
    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)


class ReviewDetail(APIView):

    def get_object(self, pk):
        try:
            return Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterAPIView(APIView):
    def get(self, request):
        register = Register.objects.all()
        serializer = ReviewSerializer(register, many=True)
        return Response(serializer.data)