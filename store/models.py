from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_category():
        return Category.objects.all()
        

#produc model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=0)
    image = models.ImageField(upload_to='media')
    description =models.CharField(max_length=300)
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:

            return Product.objects.filter(category=category_id)

        else:
            return Product.get_all_products()


class Costomer(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Costomer.objects.get(email__email=email)
        except :
            False
        

    def IsExist(self):
        if Costomer.objects.filter(email=self.email):
            return True
        return False
            
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Costomer,on_delete=models.CASCADE)
    qauntity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=250,default='',blank=True)
    mobile = models.CharField(max_length=10 ,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today())


    def placeOrder(self):
        self.save()