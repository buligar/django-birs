from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse
from .models import *


menu = [{'title': 'Войти', 'url_name': 'login'}]

def about(request):
    return render(request,'main/about.html')

def index(request):
    posts = users.objects.all()
    context = {
        'posts':posts,
        'menu': menu,
    }
    return render(request,'main/index.html',context = context)

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(users, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'main/post.html', context=context)

def show_category(request, cat_slug):
    posts = users.objects.filter(cat_slug=cat_slug)
    cats = category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug,
    }
    return render(request, 'main/index.html', context=context)
