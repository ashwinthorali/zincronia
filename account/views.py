from django.shortcuts import render, redirect
from account.forms import RegisterForm, ProfileForm, LoginForm
from django.contrib.auth.models import Group
from account.models import Profile
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.http import JsonResponse
from product.models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required
# Create your views here.
def createuser(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password1']
            profile =  profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your profile was successfully Created!')
            #authenticate checks if credentials exists in db
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
            
        else:
            messages.error(request, 'Your profile creation Failed, Try Again!')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()
    context = {
      'user_form':user_form,
      'profile_form':profile_form,
    }
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def checkup(request):
    if request.method=='GET':
        name = request.GET.get('name')
        print(name)
        c = User.objects.filter(username=name).count()
        if c > 0:
            a = 1
        else:
            a = 0
        return JsonResponse({'test':a})

@login_required(login_url='home:home')
def dashboard(request):
    data =   Order.objects.filter(user_id_id=request.user)
    context = {
        'data':data,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='home:home')
def changepw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepw.html', {
        'form': form
    })





def login_user(request):
    if request.method == "POST":
        # your sign in logic goes here
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #authenticate checks if credentials exists in db
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

                else:
                    messages.error(request, 'Incorrect Credentials.')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

            else:
                messages.error(request, 'User Does Not Exists.')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            
