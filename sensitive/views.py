from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post, Category

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    category_list = Category.objects.all()
    context = {'latest_post_list': latest_post_list, 'categories': category_list}
    return render(request, 'sensitive/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    category_list = Category.objects.all()
    context = {'post': post, 'categories': category_list}
    return render(request, 'sensitive/detail.html', context)

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category_list = Category.objects.all()
    post_list = Post.objects.filter(category = category)[:5]
    context = {'posts': post_list, 'categories': category_list}
    return render(request, 'sensitive/category.html', context)