from django.shortcuts import render, redirect
from webapp.models.product import ProductModel
from webapp.models.category import CategoryModel
from django.views import View


#print(make_password('1234'))
#print(check_password('1234',
#'pbkdf2_sha256$260000$8vRgCoUG9Q0N9KCtn1zWyj$HfCi7/5Eoi0/W25EuIlMXPBq304ejEMVhkRM1VvzltE='))
# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        print('product',product)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart',request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        
        #creating cart object
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = ProductModel.get_all_products()
        category = CategoryModel.get_all_categories()
        #print(request.GET)
        
        categoryID = request.GET.get('category')
        if categoryID:
            products = ProductModel.get_all_products_by_categoryid(categoryID)
        else:
            products = ProductModel.get_all_products()
        
        context = {}
        context['products'] = products
        context['categories'] = category

        print("You are:",request.session.get('email')) 

        return render(request, 'index.html', context)


#{{prd.feature | safe}}
