from django.urls import path
from .views import order_list, order_details

urlpatterns = [
    path('list/', order_list, name='order list'),
    path('details/', order_details, name='order details'),
]