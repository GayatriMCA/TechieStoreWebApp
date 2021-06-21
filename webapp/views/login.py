from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password
from webapp.models.customer import Customer

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                #request.session['customer_id'] = customer.id
                #request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid !!"
        else:
            error_message = "Email or Password Invalid !!"

        context = {
            'email':email,
            'error':error_message
        }

        return render(request, 'login.html', context)

def logout(request):
    request.session.clear()
    return redirect('login')