from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse  , HttpResponseRedirect
from .forms import ContactForm
# Create your views here.


def send_email(request):
    pass



def send_success(request):
    pass
