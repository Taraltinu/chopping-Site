from django.shortcuts import render,redirect
from store.models import Product,Category,Costomer
from django.views import View

class Home(View):
    def post(self,request):
        Product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(Product)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(Product)
                    else:
                        cart[Product] = quantity-1
                else:
                    cart[Product] = quantity+1
            else:
                cart[Product] = 1
        else:
            cart = {}
            cart[Product]=1
        request.session['cart'] = cart
        return redirect('/')
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products= None
        category = Category.get_all_category()
        categoryID = request.GET.get('category')
        if categoryID:

            products = Product.get_all_product_by_category_id(categoryID)
        else:
            products = Product.get_all_products()
        
        data = {}
        data['product']=products
        data['category']=category
        return render(request,'store/index.html',data)