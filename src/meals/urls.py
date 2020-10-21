from django.urls import path
from meals import views

app_name = 'meals'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail'), # <slug:slug> means the first one is type and last one is the name which we will take on the views.
]