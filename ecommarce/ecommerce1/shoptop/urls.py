from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path("home", views.home, name='home'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("contactus", views.contactus, name='contactus'),
    path("products/", views.products, name='products'),
    path("main_menu/", views.main_menu, name='main_menu'),
    path("cart", views.cart_f, name='cart'),
    path("checkout", views.checkout, name='checkout'),
    path("order_placed", views.order_placed, name='order_placed'),
    path("product/<str:sort>", views.products_sort, name='products_sort'),
    path("products/<str:filters>", views.filters, name='filter'),
    path("products/<str:filters>/<str:sort>", views.products_cate_sort, name='products_cate_sort'),
    path("product_details/<int:de_prod_id>", views.product_details, name='de_prod_id'),


]
