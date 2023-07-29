from django.shortcuts import render
from .models import Order

# Create your views here.
def home(request):
    orders = Order.objects.all()
    return render(request, 'core/home.html', {"orders": orders})
