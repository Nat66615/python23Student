from django.shortcuts import render
from .models import Product

from django.http import HttpResponse


# Create your views here.
def catalog(request):
    return HttpResponse('<h1>КАТАЛОГ</h1>')

def cart(request):
    return HttpResponse('<h1>Корзина</h1>')

def product_details(request, pid):
    return HttpResponse('<h1>Продукт</h1>')

def about(request):
    return HttpResponse('<h1>О Нас</h1>')

def payment(request):
    return HttpResponse('<h1>Оплата</h1>')







