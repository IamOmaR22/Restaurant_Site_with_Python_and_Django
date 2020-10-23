from django.urls import path
from reservation import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
]