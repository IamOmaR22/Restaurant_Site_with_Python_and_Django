from django.shortcuts import render
from reservation.models import Reservation
from . forms import ReserveTableForm

# Create your views here.

def reserve_table(request):
    return render(request, 'reservation/reservation.html')
