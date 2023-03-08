from django.shortcuts import render, redirect 
from django.contrib.auth.models import User        
from django.contrib.auth import login, authenticate, logout  
from django.conf import settings  
from django.core.mail import send_mail 
from webempresa.settings import EMAIL_HOST_USER 
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm
    return render(request, "contact/contact.html", {'form': contact_form})

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        
        login(request, user)
        subject = 'Bienvenido a LENOTECA'
        message = f'Hola {user.username}, Gracias por Contactarnos.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [user.email,]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/contact/')
    
    return render(request, 'contact.html' )
