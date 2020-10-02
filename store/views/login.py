from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models import Product,Category,Costomer
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,'store/login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Costomer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer'] = email
                return redirect('home')
            else:
                error_message = "Email or Password in Invalid"
        else:
            error_message = "Email or Password in Invalid"
        return render(request,'store/login.html',{'error':error_message})



def logout(request):
    request.session.clear()
    return redirect('home')