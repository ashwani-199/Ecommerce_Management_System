from fronts.home.models import CartItem

def cart(request):
    cart = CartItem.objects.filter().all()
    
    if cart is None:
        return {'cart_count': None}
    else:
        return {'cart_count': cart.count()}
    