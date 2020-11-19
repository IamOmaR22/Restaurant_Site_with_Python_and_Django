from django.shortcuts import render
from meals.models import Meals

def home(request):

    meals = Meals.objects.all()
    
    context = {
        'meals' : meals ,        
    }

    return render(request, 'home/index.html', context)
