from django.shortcuts import render
from interface.models import Product
from core.models import Profile
from django.contrib.auth.decorators import login_required

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

def profile(request):
    profiles = Profile.objects.all()
    return render(
        request,
        'interface/profile.html',
        {
            "profiles": profiles
        }
    )

@login_required
def auth(request):
    return render(
        request,
        'interface/auth.html'
    )