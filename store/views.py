from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'store/index.html')


#listing 
"""def listing(request):
    return render(request, 'store/listing.html')"""