from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Main Page')

def test_page(request):
    return HttpResponse('Test', status=404)

def get_contacts(request):
    return HttpResponse('Это контакты')

def get_about(request):
    return HttpResponse('Это страница about')

