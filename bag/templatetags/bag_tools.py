from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(starting_price, quantity):
    return starting_price * quantity
