from django.views import View
from django.shortcuts import render,redirect
from store.models import Product,Order,Costomer



class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(address,mobile,customer,cart,products)

        for product in products:
            order = Order(customer = Costomer(id = customer),
                        product=product,
                        price = product.price,
                        address= address,
                        mobile = mobile,
                        qauntity = cart.get(str(product.id)))
            order.placeOrder()       
        return redirect('cart') 