from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models import Product,Category,Costomer
from django.views import View
# from .forms import book1


class Signup(View):
    def get(self,request):
        return render(request,'store/signup.html')
    def post(self , request):

        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        value ={
            'fullname':fullname,
            'phone':phone,
            'email':email
        }
        customer = Costomer(fullname=fullname,
                phone=phone,
                email=email,
                password=password)
        error_message = None

        error_message = self.validate_Customer(customer)
        
        if not  error_message:
            customer.password= make_password(customer.password)
            customer.save()
            return redirect('home')
        else:
            data = {
                'error':error_message,
                'value':value
            }
            return render(request,'store/signup.html',data)



    def validate_Customer(self,customer):
            error_message = None
            if not (customer.fullname):
                error_message = "Full name is Required"
            elif len(customer.fullname) < 4:
                error_message = "Full name must be more then 4"
            elif not customer.phone:
                error_message = "phone Number is Required"
            elif len(customer.phone) != 10:
                error_message = "phone number must be 10 digit"
            elif not customer.email:
                error_message = "email Field is Required"
            elif not customer.password:
                error_message = "password field is required"
            # elif customer.password !=repassword:
            #     error_message = "password Not Matches"
            # elif customer.IsExist:
            #     error_message = "Email Address Is Already Exist"
            return error_message