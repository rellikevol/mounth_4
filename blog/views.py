from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def get_contacts(request):
    return render(request, 'blog/contacts.html')

def get_about(request):
    return render(request, 'blog/about.html')

