from apps.shipping_cart.cart import Cart

def cart(request):
    
    return {'cart': Cart(request)}