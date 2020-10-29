from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'post/post_list.html', {'post_list':post_list})


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)

    return render(request, 'post/post_detail.html', {'post_detail':post_detail})

