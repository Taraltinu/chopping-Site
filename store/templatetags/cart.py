from django import template

register  =template.Library()

@register.filter(name ='is_in_cart')
def is_in_cart(pd , cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==pd.id:
            return True
    return False

@register.filter(name ='cart_Quantity')
def cart_Quantity(pd , cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==pd.id:
            return cart.get(id)
    return 0


@register.filter(name ='price_total')
def price_total(pd , cart):
   return pd.price * cart_Quantity(pd, cart)

@register.filter(name ='total_cart_price')
def total_cart_price(pd,cart):
    sum=0
    for p in pd:
        sum +=price_total(p,cart)

    return sum
