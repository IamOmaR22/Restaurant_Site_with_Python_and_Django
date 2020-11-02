from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'post/post_list.html', {'post_list':post_list})


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()

    return render(request, 'post/post_detail.html', {'post_detail':post_detail, 'categories':categories})


def post_by_tag(request, tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])  # Here tags is the name of model field 
    context = {
        'post_list' : post_by_tag ,
    }

    return render(request , 'post/post_list.html' , context)



def post_by_category(request, category):
    post_by_category = Post.objects.filter(category__category_name=category)  # Here category is the name of model field 
    context = {
        'post_list' : post_by_category ,
    }

    return render(request , 'post/post_list.html' , context)