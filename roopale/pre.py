from product.models import *



def allpage(request):
    topmenu = TopMenu.objects.all().order_by('order')
    submenu = SubMenu.objects.all().order_by('order')
    wishlistItemCount = 0
    cartDataCount = 0
    
    if request.user.is_authenticated:
        uid = request.user.id
        wishlistItemCount =  Wishlist.objects.filter(user=uid).count()
        cartDataCount = Cart.objects.filter(user=uid).count()
        
           



    context = {
        'topmenu':topmenu,
        'submenu':submenu,
        'wishlistItemCount':wishlistItemCount,
        'cartDataCount':cartDataCount,
        
    }
    return context