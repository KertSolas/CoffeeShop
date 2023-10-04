from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'navbar.html', {'page_title': 'Home Page', 'page_content': 'Welcome to the Home Page'})

def about(request):
    return render(request, 'navbar.html', {'page_title': 'About Page', 'page_content': 'This is the About Page'})

def contact(request):
    return render(request, 'navbar.html', {'page_title': 'Contact Page', 'page_content': 'Contact us here'})
