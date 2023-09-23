from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'finalexam/home.html', context)

def products(request):
    context = {}
    return render(request, 'finalexam/products.html', context)

def about(request):
    context = {}
    return render(request, 'finalexam/about.html', context)

def login(request):
    context = {}
    return render(request, 'finalexam/login.html', context)
