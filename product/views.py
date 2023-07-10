from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.http import JsonResponse,HttpResponse
import razorpay
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from rest_framework.decorators import api_view

from django.conf import settings
import stripe


# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


# C
from django.views.decorators.csrf import csrf_exempt
client = razorpay.Client(auth=("rzp_test_BAFmlfpAivgV6F", "KoJLJSBgmGnxCwUxfMXYyzoY"))
def product(request):
    context = {

    }
    return render(request, 'product_list.html', context)

@login_required(login_url='/')
def mywishlist(request):
    uid =request.user.id
    data = Wishlist.objects.filter(user=uid)
    data1 = Products.objects.all().order_by('order')[:8]
    context = {
        'data':data,
        'data1':data1,
    }
    return render(request, 'mywishlist.html', context)


@login_required(login_url='/')
def mycart(request):
    uid = request.user.id
    cartData = Cart.objects.filter(user=uid)
    totalPrice = 0
    final_discount = 0
    q = 1
    for ie in cartData:
        totalPrice = totalPrice + int(ie.price) * int(ie.qty)
    final_amount = totalPrice
    # check coupon code
    if request.method=='POST':
        print('test')
        q = request.POST.get('q')
        q = str(q)
        print(q)
        try:
            data = CouponCode.objects.get(code=q) 
            print(data)
            # membership or giftcards
            if data.one_user:
                # is code valid
                data2 = CouponCode.objects.filter(code=q, user=uid).count()
                pid = data.id
                if data2 > 0:
                    check = CouponCodeUsage.objects.filter(coupon=pid, user=uid, used=True).count()
                    if check >= data.times:
                        print('fail', check)
                        messages.error(request, 'Coupon Already Used')

                    else:
                        coupon_save = CouponCodeUsage.objects.create(coupon=data, user=request.user, used=False)
                        discount_precentage =int(data.discount)
                        totalDiscount = (discount_precentage/100)*totalPrice; 
                        
                        if totalDiscount > data.max_sp_discount:
                            final_discount = data.max_sp_discount
                        else:
                            final_discount = totalDiscount
                
                        final_amount = totalPrice - final_discount 
            
            # general 
            else:
                pid = data.id
                check = CouponCodeUsage.objects.filter(coupon=pid, user=uid, used=True).count()
                if check >= data.times:
                    print('fail', check)
                    messages.error(request, 'Coupon Already Used')
                else:
                    
                    coupon_save = CouponCodeUsage.objects.create(coupon=data, user=request.user, used=False)
                    discount_precentage =int(data.discount)
                    totalDiscount = (discount_precentage/100)*totalPrice; 
                    
                    if totalDiscount > data.max_sp_discount:
                        final_discount = data.max_sp_discount
                    else:
                        final_discount = totalDiscount
            
                    final_amount = totalPrice - final_discount                 
            
        except:
            q = 1
            messages.error(request, 'Invalid Coupon')  
            return redirect('product:mycart')          

    uid =request.user.id
    data = Cart.objects.filter(user=uid)
    print(q)
    context = {
        'data':data,
        'totalPrice':totalPrice,
        'final_discount':final_discount,
        'final_amount':final_amount,
        'q':q,
    }
    return render(request, 'mycart.html', context)


@login_required(login_url='/')
def paymentMethod(request):
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data_price = form.save(commit=False)
            uid = request.user.id
            cartData = Cart.objects.filter(user=uid)
            totalPrice = 0
            final_discount = 0
            q = 1
            for ie in cartData:
                totalPrice = totalPrice + int(ie.price) * int(ie.qty)
            final_amount = totalPrice
            # check coupon code
            if request.method=='POST':
                print('test')
                q = request.POST.get('coupon_code')
                q = str(q)
                print(q)
                try:
                    data = CouponCode.objects.get(code=q) 
                    print(data)
                    # membership or giftcards
                    if data.one_user:
                        # is code valid
                        data2 = CouponCode.objects.filter(code=q, user=uid).count()
                        pid = data.id
                        if data2 > 0:
                            check = CouponCodeUsage.objects.filter(coupon=pid, user=uid, used=True).count()
                            if check >= data.times:
                                print('fail', check)
                                messages.error(request, 'Coupon Already Used')

                            else:
                                coupon_save = CouponCodeUsage.objects.create(coupon=data, user=request.user, used=False)
                                discount_precentage =int(data.discount)
                                totalDiscount = (discount_precentage/100)*totalPrice; 
                                
                                if totalDiscount > data.max_sp_discount:
                                    final_discount = data.max_sp_discount
                                else:
                                    final_discount = totalDiscount
                        
                                final_amount = totalPrice - final_discount 
                    
                    # general 
                    else:
                        pid = data.id
                        check = CouponCodeUsage.objects.filter(coupon=pid, user=uid, used=True).count()
                        if check >= data.times:
                            print('fail', check)
                            messages.error(request, 'Coupon Already Used')
                        else:
                            
                            coupon_save = CouponCodeUsage.objects.create(coupon=data, user=request.user, used=False)
                            discount_precentage =int(data.discount)
                            totalDiscount = (discount_precentage/100)*totalPrice; 
                            
                            if totalDiscount > data.max_sp_discount:
                                final_discount = data.max_sp_discount
                            else:
                                final_discount = totalDiscount
                    
                            final_amount = totalPrice - final_discount                 
                    
                except:
                    pass
                
                print(final_amount, final_discount)
                data_price.total_amount = int(final_amount)
                data_price.discount = int(final_discount)
                data_price.save()

            messages.success(request, 'Order Created Successfully')
            return render(request, 'stripe/payment.html')
        else:
            print(form.errors)

    context = {

    }
    return render(request, 'payment_method.html', context)


@login_required(login_url='/')
def paymentMethodSelected(request):
    uid = request.user.id
    data = Order.objects.filter(user_id=uid).last()
    print(data)
    method_type =''
    if request.method=="POST":
        form = PaymentMethodForm(request.POST, instance=data)
        if form.is_valid():
            method_type = form.cleaned_data['payment_method']
            print('method_type', method_type    )
            method_type = str(method_type) 
            form.save()
        else:
            print(form.errors)

    context = {

    }
    if method_type == 'razor':
        data = Order.objects.filter(user_id=uid).last()
        amount = int(data.total_amount) *100
        notes = {
                'welcome': 'Welcome to studyatmit.com'
            }
        response = client.order.create(dict(amount=amount, currency='INR', receipt='order_receipt', notes=notes, payment_capture='0'))
        order_id = response['id']
        order_status = response['status']
        data.payment_id = (order_id)
        data.save()
        data2= Cart.objects.filter(user=uid)
        context = {
            'data':data,
            'amount':amount,
            'data2':data2,
            'order_id':order_id,
                    
        }
        return render(request, 'complete_purchase.html', context)
    elif method_type == 'stripe':
        amount = int(data.total_amount) *100
        data = Order.objects.filter(user_id=uid).last()
        context = {
            'amount':amount,
            'data':data,    
        }

        return render(request, 'stripe/payment.html', context)

    
    else:
        pass

@csrf_exempt
def payment_status(request):

    response = request.POST

    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    for key , val in response.items():
        if key == "razorpay_order_id":
            order_id = val
            break
    user = Order.objects.filter(payment_id=order_id).first()
    user.paid = True
    uid = request.user.id
    cart = Cart.objects.filter(user=uid)
    cart_dict = {"name":[], "qty":[]}
    a = cart_dict["name"]
    for ie in cart:
        if a:
            for i in a:
                if ie.product.product_name in cart_dict["name"]:
                    pass
                else:
                    cart_dict["name"].append(ie.product.product_name)
                    cart_dict["qty"].append(ie.qty) 
                    
        else:
            cart_dict["name"].append(ie.product.product_name)
            cart_dict["qty"].append(ie.qty)     
        ie.delete()    

    print(cart_dict)
    user.bill = cart_dict    
    
    user.save() 
    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})

@csrf_exempt
def payWithStripe(request):
    uid = request.user.id
    mydata = Order.objects.filter(user_id=uid).last()
    print(request.POST)
    
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'Cart Checkout',
        },
        'unit_amount': int(mydata.total_amount) *100,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url= YOUR_DOMAIN + "/products/pay-with-stripe-confirmation?session_id={CHECKOUT_SESSION_ID}",
    cancel_url=YOUR_DOMAIN + '/products/mycart/',
    )
    return JsonResponse({'id': session.id})


@csrf_exempt
@api_view(['GET'])
def payWithStripeConfirmation(request):
    q = request.GET.get('session_id')
    uid = request.user.id
    session = stripe.checkout.Session.retrieve(q)
    customer = stripe.Customer.retrieve(session.customer)
    print(session)
    for key, val in session.items():
        print(key,'-->',val)
        if key == 'payment_intent':
            order_id = val
        if key == 'amount_total':
            amount = val
    print(order_id)
    amount = int(amount)/100
    response = request.POST
    user = Order.objects.filter(user_id=uid, total_amount=amount).last()
    user.paid = True
    user.payment_id = order_id
    uid = request.user.id
    cart = Cart.objects.filter(user=uid)
    cart_dict = {"name":[], "qty":[]}
    a = cart_dict["name"]
    for ie in cart:
        if a:
            for i in a:
                if ie.product.product_name in cart_dict["name"]:
                    pass
                else:
                    cart_dict["name"].append(ie.product.product_name)
                    cart_dict["qty"].append(ie.qty) 
                    
        else:
            cart_dict["name"].append(ie.product.product_name)
            cart_dict["qty"].append(ie.qty)     
        ie.delete()    

    print(cart_dict)
    user.bill = cart_dict    
    
    user.save() 
    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})



def product_list(request, pk):
    data1 = Products.objects.filter(sub_menu_name__slug=pk).order_by('order')
    top = Products.objects.filter(sub_menu_name__slug=pk).order_by('-id')[:3]
    q = SubMenu.objects.get(slug=pk)
    page_name = q.sub_menu_name
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 6)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    context = {
        'data':data,
        'page_name':page_name,
        'top':top,
        'seo':q,
    }
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    seo = Products.objects.get(slug=pk)
    if seo.sub_menu_name:
        q = seo.sub_menu_name.id
        submenu = True
        data = Products.objects.filter(sub_menu_name__id=q).order_by('order')[:8]
    else:
        submenu = None
        data = Products.objects.all().order_by('order')[:8]
    print(data)
    context = {
        'seo':seo,
        'data':data,
        'submenu':submenu,
    }
    return render(request, 'product_detail.html', context)


def addtocart(request, pk):
    uid = request.user
    pid = Products.objects.get(id=pk)
    shade = request.GET.get('shade')
    spec = request.GET.get('spec')
    sp = request.GET.get('sp')
    
    sp = int(sp)
    minus = request.GET.get('minus')
    if minus:
        pass
    else:
        minus = 0    
    print(sp)
    item = 0
    cart_id = 0
    if sp == 1:
        price = Products.objects.get(id=pid.id)
        price = int(price.sp)
    else:
        price = MapPriceList.objects.get(product=pid, shade=shade, specification=spec)
        price = int(price.mrp)
    c = Cart.objects.filter(user=uid, product=pid).count()
    if c > 0:
        if sp == 1:
            data = Cart.objects.get(user=uid, product=pid, price=price)
            cart_id = data.id
            q = data.qty
            if int(minus) == -1:
                if q is None:
                    q = 0
                else:
                    q = int(q)    
                data.qty = q - 1
                data.save()
                item = q - 1
            else:
                if q is None:
                    q = 0
                else:
                    q = int(q)    
                data.qty = q + 1
                data.save()
                item = q + 1
        else:
            price_check = Cart.objects.filter(user=uid, product=pid, spec = int(spec), shade = int(shade), price=price).count() 
            print('###abc', price_check)
            if price_check > 0:
                data = Cart.objects.filter(user=uid, product=pid).count()
                print('#data',data)
                data = Cart.objects.get(user=uid, product=pid, spec = int(spec), shade = int(shade), price=price)  
                data.save()
                cart_id = data.id
                q = data.qty
                print(q)
                if int(minus) == -1:
                    if q is None:
                        q = 0
                    else:
                        q = int(q)    
                    data.qty = q - 1
                    data.save()
                    item = q - 1
                else:
                    if q is None:
                        q = 0
                    else:
                        q = int(q)    
                    data.qty = q + 1
                    data.save()
                    item = q + 1
            else:
                data = Cart.objects.filter(user=uid, product=pid).count()
                print(data)
                if data > 0:
                    data = Cart.objects.get(user=uid, product=pid)
                    data.delete()
                data = Cart.objects.create(user=uid, product=pid, qty=0, spec = int(spec), shade = int(shade), price=price)  
                data.save()
                cart_id = data.id
                q = data.qty
                print(q)
                if int(minus) == -1:
                    if q is None:
                        q = 0
                    else:
                        q = int(q)    
                    data.qty = q - 1
                    data.save()
                    item = q - 1
                else:
                    if q is None:
                        q = 0
                    else:
                        q = int(q)    
                    data.qty = q + 1
                    data.save()
                    item = q + 1

    else:
        if sp == 1:
            Cart.objects.create(user=uid, product=pid, qty=1,  price=price)  
            item = 1
            items = Cart.objects.get(user=uid, product=pid)
            cart_id = items.id
        else:

            Cart.objects.create(user=uid, product=pid, qty=1, spec = int(spec), shade = int(shade), price=price)  
            item = 1
            items = Cart.objects.get(user=uid, product=pid, spec = int(spec), shade = int(shade))
            cart_id = items.id

    new_val = Cart.objects.filter(user=uid).count()
    b =  pid.id
    return JsonResponse({'items':item, 'pid':b, 'cart_id':cart_id,'new_val':new_val, 'sp':sp})
    
    

def deletecart(request, pk):
    uid = request.user.id
    pid = Products.objects.get(id=pk)
    obj = Cart.objects.get(user=uid, product=pid)
    b = obj.product.id
    item = 0
    cart_id = 'abc'
    obj.delete()
    new_val = Cart.objects.filter(user=uid).count()
    return JsonResponse({'new_val':new_val})
    

def getprice(request):
    if request.method == 'GET':
        print('ya')
        shade = int(request.GET.get('shade'))
        spec = int(request.GET.get('spec'))
        product = int(request.GET.get('product'))
        price = MapPriceList.objects.get(shade__id=shade, specification__id=spec, product__id=product)
        mrp =  int(price.mrp)
        print(mrp)


    return JsonResponse({'mrp':mrp})
    


def increaseItem(request, pk):
    if request.method == 'GET':
        uid = request.user
        pid = request.GET.get('pid')
        print(pid)
    else:
        print('error')    
    
    c = Cart.objects.filter(user=uid, product=pid).count()
    q = 0
    if c > 0:
        obj = Cart.objects.get(id=pk)
        q = int(obj.qty)
        q = q + 1
        b = obj.product.id

        instock = obj.product.in_stock
        if instock >= q:
            obj.qty = q
        else:
            q = q -1
        item = 0
        cart_id = obj.id
        obj.save()
        qty = q
    
    else:
        b = Products.objects.get(id=pid)
        Cart.objects.create(user=uid, product=b, qty=1)  
        item = 1
        items = Cart.objects.get(user=uid, product=pid)
        cart_id = items.id 
        q = 1
        b = b.id


    
    return JsonResponse({'items':item, 'pid':b, 'cart_id':cart_id, "qty":q})


def deleteWishlistItem(request, pk):
    uid = request.user.id
    try:
        obj = Wishlist.objects.get(id=pk, user=uid)
        obj.delete()
    except:
        pass
    messages.success(request, 'Successfully Removed')
    return redirect('product:wishlist')    
# return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
def deleteCartItem(request, pk):
    uid = request.user.id
    try:
        obj = Cart.objects.get(id=pk, user=uid)
        obj.delete()
    except:
        pass
    messages.success(request, 'Successfully Removed')
    return redirect('product:mycart')    


def decreaseItem(request, pk):
    if request.method == 'GET':
        uid = request.user
        pid = request.GET.get('pid')
        print(pid)
    else:
        print('error')    
    
    c = Cart.objects.filter(user=uid, product=pid).count()
    if c > 0:
       
        obj = Cart.objects.get(id=pk)
        q = int(obj.qty)
        q = q - 1
        b = obj.product.id

        instock = obj.product.in_stock
        if q > 0:
            obj.qty = q
            obj.save()
        
        elif q == 0:
                obj.delete()
        
        else:
            q = q + 1
        
        item = 0
        cart_id = obj.id
        qty = q
        return JsonResponse({'items':item, 'pid':b, 'cart_id':cart_id, "qty":q})
    else:
        return JsonResponse({'items':'0'})



def addtowishlist(request, pk):
    uid = request.user
    pid = Products.objects.get(id=pk)
    item = 0
    flag = 0
    
    c = Wishlist.objects.filter(user=uid, product=pid).count()
    if c < 1:
        d = Wishlist.objects.create(user=uid, product=pid)
        d = d.save()
        flag = 1
    else:
        d = Wishlist.objects.get(user=uid, product=pid)
        d.delete()

    pid = int(pid.id)    
    new_val = Wishlist.objects.filter(user=uid).count()
    
    # wishlist-counter
    return JsonResponse({'items':item, 'pid':pid, 'flag':flag, 'new_val':new_val})
    
    

def add_review(request):
    if request.method == 'POST':
        print('###hey')
        stars = request.POST.get('stars')
        message  = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        product = request.POST.get('product')
        product = Products.objects.get(id=str(product))
        data = Reviews.objects.create(name=name, email=email, stars=stars, product=product, comment=message)
        messages.success(request, 'Reivew Posted Successfully')
        data.save

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        pass

def newsletter(request):
    if request.method == 'POST':
        print('###hey')
        email = request.POST.get('email')
        data = NewsLetter.objects.create(email=email)
        messages.success(request, 'Newsletter Subscribed Successfully')
        data.save

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def search_product(request):
    if request.method =='GET':
        q = request.GET.get('q')
        data1 = Products.objects.filter(product_name__contains=q)
        query = q
        q = True
        print(data1)
        if data1:
            pass
        else:       
            data1 = Products.objects.all()
            q = False
        
        top = Products.objects.all().order_by('-id')[:3]
        page = request.GET.get('page', 1)

        
        paginator = Paginator(data1, 8)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        context = {
            'data':data,
            'top':top,
            'q':q,
            'search':True,
            'query':query,
        }
        return render(request, 'product_list.html', context)


def allproduct(request):
        data1 = Products.objects.all()
        q = False
        
        top = Products.objects.all().order_by('-id')[:3]
        page = request.GET.get('page', 1)

        
        paginator = Paginator(data1, 8)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        context = {
            'data':data,
            'top':top,
            'q':q,
            'search':True,
            'query':'All Products',
        }
        return render(request, 'product_list.html', context)
