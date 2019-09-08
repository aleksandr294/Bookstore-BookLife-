from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    prod=Product.objects.filter(is_active=True)
    return render(request, 'products/products.html', locals())
