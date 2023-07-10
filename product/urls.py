from django.urls import path
from . import views
app_name='product'
urlpatterns = [
    path('get-price/', views.getprice, name='getprice'),
    path('wishlist/', views.mywishlist, name='wishlist'),
    path('mycart/', views.mycart, name='mycart'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('paymentMethod/', views.paymentMethod, name='createOrder'),
    path('add-new-review/', views.add_review, name='add_review'),
    path('pay/', views.paymentMethodSelected, name='paymentMethodSelected'),
    path('payment_status', views.payment_status, name = 'payment_status'),
    path('pay-with-stripe/', views.payWithStripe, name='payWithStripe'),
    path('pay-with-stripe-confirmation', views.payWithStripeConfirmation, name='payWithStripeConfirmation'),
    
    path('search-product/', views.search_product, name='search_product'),
    path('all-product/', views.allproduct, name='allproduct'),
    path('<str:pk>/', views.product_list, name='product_list'),
    path('shop/<str:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<str:pk>/', views.addtocart, name='addtocart'),
    path('remove-from-cart/<str:pk>/', views.deletecart, name='deletecart'),
    path('increase-item/<str:pk>/', views.increaseItem, name='increaseItem'),
    path('decrease-item/<str:pk>/', views.decreaseItem, name='decreaseItem'),
    path('add-to-wishlist/<str:pk>/', views.addtowishlist, name='addtowishlist'),
    path('remove-from-wishlist/<str:pk>/', views.deleteWishlistItem, name='deleteWishlistItem'),
    path('remove-items-from-wishlist/<str:pk>/', views.deleteCartItem, name='deleteCartItem'),

] 