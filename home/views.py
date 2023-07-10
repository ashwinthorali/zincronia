from django.shortcuts import render, redirect
from seo.models import AboutPage,Team,Testimonials
from product.models import *
from blog.models import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.
def home(request):
    trending = Products.objects.filter(trending=True).order_by('-order')[:10]
    featured = Products.objects.filter(featured=True).order_by('-order')[:10]
    new_arrival = Products.objects.filter(featured=True).order_by('-order')[:10]
    best_seller = Products.objects.filter(best_seller=True).order_by('-order')[:10]
    client_review = Testimonials.objects.all().order_by('-id')[:7]
    blog = Blog.objects.all().order_by('-id')[:7]
    context = {
        'trending':trending,
        'new_arrival':new_arrival,
        'featured':featured,
        'best_seller':best_seller,
        'client_review':client_review,
        'blog':blog,
    }
    return render(request, 'index.html', context)


def about(request):
    seo = AboutPage.objects.first()
    team = Team.objects.all().order_by('-id')[:4]
    client_review = Testimonials.objects.all().order_by('-id')[:7]
    print(seo)
    context = {
        'seo':seo,
        'team':team,
        'client_review':client_review,
    }
    return render(request, 'about.html', context)    

def contact(request):
    seo = AboutPage.objects.first()
    team = Team.objects.all().order_by('-id')[:4]
    client_review = Testimonials.objects.all().order_by('-id')[:7]
    print(seo)
    context = {
        'seo':seo,
        'team':team,
        'client_review':client_review,
    }
    return render(request, 'contact.html', context)    


def gallery(request):
    data = Gallery.objects.all().order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'gallery.html', context)    


def byebye(request):
    logout(request)
    return redirect('home:home')

