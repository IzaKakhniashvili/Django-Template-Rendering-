from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Category, Product

# Create your views here.


def home_page(request):
    return render(request, 'index.html')

def product_list(request, slug):
    return render(request, 'shop.html')

def product_detail(request, slug):
    return render(request, 'shop-detail.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'chackout.html')

def contact(request):
    return render(request, 'contact.html')