from django.shortcuts import render
from interface.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(
        request,
        'core/home.html',
        {
            "products": products

        }
    )
