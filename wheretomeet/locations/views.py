from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    if request.method  =="POST":
        people = request.POST.get('people')
        return redirect('locations:search', people)
    else:
        return render(request, 'locations/index.html')



def search(request,people):
    context={
        'people': people
    }
    return render(request, 'locations/search.html', context)

def result(request):
    return render(request, 'locations/result.html')