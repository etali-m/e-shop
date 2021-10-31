from django.shortcuts import render
import random

from .models import *

# Create your views here.
def index(request):
    tags = Tag.objects.all()[:7]
    tag_list = list(Tag.objects.all())
    random_tags = random.sample(tag_list, 3)
    categories = Category.objects.all()
    context = {'categories':categories, 'random_tags': random_tags, 'tags': tags}
    return render(request, 'store/index.html', context)

def product(request): 
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/products.html', context)

def service(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    context = {'services': services, 'categories':categories}
    return render(request, 'store/services.html', context)

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html')

def cart(request):
    return render(request, 'store/cart.html')

def blog(request):
    pass