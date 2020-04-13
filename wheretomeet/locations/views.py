from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'locations/index.html')

def result(request):
    pass