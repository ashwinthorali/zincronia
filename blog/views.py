from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def blog_home(request):
    data1 = Category.objects.all().order_by('id')[:9]
    data2 = Blog.objects.all().order_by('-id')[:3]
    context = {
        'data1':data1,
        'data2':data2,
    }
    return render(request, 'blog_home.html', context)

def blog_list(request):
    data1 = Blog.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 9)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'data':data,
    }
    return render(request, 'blog_list.html', context)

def bs(request):
    from_search = True
    q='q'
    if request.method=="GET":
        q = request.GET.get('q')
    else:
        q= "a"    
    print(q)
    if q is None:
        q =''
           
    data1 = Blog.objects.filter(Q(content__contains=q) | Q(h1__contains=q)).order_by('-id')
    if data1:
        print('a')
        page = request.GET.get('page', 1)
        paginator = Paginator(data1, 9)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

    else:
        data1 = Blog.objects.filter(content__contains="a").order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(data1, 9)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

    context = {
        'data':data,
        'from_search':from_search,
        'q':q,
    }
    return render(request, 'blog_list.html', context)


def cat_list(request, pk):
    
    data1 = Blog.objects.filter(category__id=pk).order_by('-id')
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 9)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'data':data,
    }
    return render(request, 'blog_list.html', context)


def blog_detail(request, pk):
    data = Blog.objects.get(slug=pk)
    blog_id = data.id
    data1 = Category.objects.all().order_by('id')[:9]

    next_post = blog_id + 1
    prev_post = blog_id - 1
    recent_blog = Blog.objects.all().order_by('-id')[:5]
    try:
        np = Blog.objects.get(id=next_post)
    except:
        np = None    
    
    try:
        pp = Blog.objects.get(id=prev_post)
    except:
        pp = None    
      



    context = {
        'data':data,
        'np':np,
        'pp':pp,
        'data1':data1,
        'recent_blog':recent_blog,
    }
    return render(request, 'blog_detail.html', context)
