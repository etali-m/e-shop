from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/products.html', context)

def service(request):
    pass

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html')

def cart(request):
    return render(request, 'store/cart.html')

def blog(request):
    pass