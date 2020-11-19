from django.shortcuts import render
from meals.models import Meals, Category

def home(request):

    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    
    context = {
        'meals' : meals,      
        'meal_list' : meal_list,
        'categories' : categories,  
    }

    return render(request, 'home/index.html', context)
