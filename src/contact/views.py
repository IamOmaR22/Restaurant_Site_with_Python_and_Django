from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass    

    else:
        form = ContactForm()

    context = {
        'form' : form
    }

    return render(request , 'contact/contact.html', context)



def send_success(request):
    return HttpResponse('thanks you for you email ^_^')
