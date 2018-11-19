from django.shortcuts import render

from .models import Product


def all_products(request):
    products = Product.object.all
    return render(request, "products.html", {products:product})
