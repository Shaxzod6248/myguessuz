from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import (CategoryAPIView, ProductsAPIView, BannerAPIView, ReviewAPIView, AboutusAPIView, FotogalleryAPIView, SubcategoryAPIView,
                    CategoriesDetail, ProductDetail, BannerDetail, AboutusDetail, ReviewDetail, FotogalleryDetail, SubcategoryDetail)


urlpatterns = [
    path('fotogallery/', FotogalleryAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('subcategory/', SubcategoryAPIView.as_view()),
    path('products/', ProductsAPIView.as_view()),
    path('banners/', BannerAPIView.as_view()),
    path('aboutus/', AboutusAPIView.as_view()),
    path('review/', ReviewAPIView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('categories/<int:pk>/', CategoriesDetail.as_view()),
    path('banners/<int:pk>/', BannerDetail.as_view()),
    path('aboutus/<int:pk>/', AboutusDetail.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('fotogallery/<int:pk>/', FotogalleryDetail.as_view()),
    path('subcategory/<int:pk>/', SubcategoryDetail.as_view()),
]