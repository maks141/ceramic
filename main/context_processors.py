from cart.cart import Cart
from cart.forms import CartAddProductForm
from .forms import CartForm

def product_cart_context(request):
    cartForm = CartForm()
    cart = Cart(request)
    len_product = 0
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
        len_product += 1
    return ({'cart' : cart, 'len_product' : len_product, 'cartForm' : cartForm})