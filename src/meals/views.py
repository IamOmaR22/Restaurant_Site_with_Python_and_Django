from django.shortcuts import render
from .models import Meals

# Create your views here.

def meal_list(request):
    meal_list = Meals.objects.all()
    return render(request, 'meals/meal_list.html', {'meal_list': meal_list, })


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug) # slug=slug means the first one is model field and last one is which we pass from url.
    return render(request, 'meals/meal_detail.html', {'meal_detail': meal_detail, })