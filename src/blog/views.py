from django.shortcuts import render
from .models import Post, Category, Comment
from taggit.models import Tag
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 5) # Show 5 posts per page

    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    return render(request, 'post/post_list.html', {'post_list':post_list})


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()

    comments = Comment.objects.filter(post=post_detail)

    if request.method == 'POST' :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'post_detail' : post_detail,
        'categories' : categories,
        'all_tags' : all_tags,
        'comments' : comments,
        'comment_form' : comment_form,
    }

    return render(request, 'post/post_detail.html', context)


def post_by_tag(request, tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])  # Here tags is the name of model field 
    context = {
        'post_list' : post_by_tag ,
    }

    return render(request , 'post/post_list.html' , context)



def post_by_category(request, category):
    post_by_category = Post.objects.filter(category__category_name=category)  # Here category_name is the name of Category model's field
    context = {
        'post_list' : post_by_category,
    }

    return render(request , 'post/post_list.html', context)