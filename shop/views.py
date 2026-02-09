from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def home(request):
    return render(request, 'shop/home.html')

def product_list_api(request):
    # This fetches all products from your database for Rabiatul Aqmal Store
    products = Product.objects.all().values('id', 'name', 'price', 'description')
    return JsonResponse(list(products), safe=False)