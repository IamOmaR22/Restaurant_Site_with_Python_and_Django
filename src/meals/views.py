from django.shortcuts import render
from .models import Meals, Category

# Create your views here.

def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    return render(request, 'meals/meal_list.html', {'meal_list': meal_list, 'categories': categories,})


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug) # slug=slug means the first one is model field and last one is which we pass from url.
    return render(request, 'meals/meal_detail.html', {'meal_detail': meal_detail, })