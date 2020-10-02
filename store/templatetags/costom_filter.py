from django import template

register  =template.Library()


@register.filter(name ='currncy')
def currncy(number):
    return "₹" + str(number)
   