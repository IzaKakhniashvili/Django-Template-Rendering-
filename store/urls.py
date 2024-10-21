from django.urls import path
from .views import home_page, product_list, cart, checkout, contact, product_detail

urlpatterns = [
    path('', home_page, name='home_page'),
    path('category/<slug:slug>/', product_list, name='poduct list'),
    path('product/<slug:slug>/', product_detail, name = "product details" ),
    path('order/cart/', cart, name = "cart"),
    path('order/checkout/', checkout, name = "checkout"),
    path('contact/', contact, name = 'contact'),
]