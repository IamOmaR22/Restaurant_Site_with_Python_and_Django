from django.shortcuts import render
from .models import Meals

# Create your views here.

def meal_list(request):
    meal_list = Meals.objects.all()
    return render(request, 'meals/meal_list.html', {'meal_list': meal_list, })


def meal_detail(request, slug):
    pass
