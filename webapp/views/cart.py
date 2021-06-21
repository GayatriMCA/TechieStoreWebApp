from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password
from webapp.models.product import ProductModel

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products_details = ProductModel.get_products_by_id(ids)
        print(products_details)
        return render(request, 'cart.html', {'products_details':products_details})