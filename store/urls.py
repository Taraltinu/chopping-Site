from django.urls import path
from store.views import login,home,signup,cart,checkout
from django.conf import settings
from django.conf.urls.static import static
# from store.views.login import Login


urlpatterns=[
    path('',home.Home.as_view(), name="home"),
    path('signup',signup.Signup.as_view(),name="signup"),
    path('login',login.Login.as_view(),name="login"),
    path('logout',login.logout),
    path('cart',cart.Cart.as_view(), name='cart'),
    path('checkout',checkout.CheckOut.as_view(), name='checkout'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)