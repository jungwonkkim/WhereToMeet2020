from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .mypath import searchx, searchy, time
import json
# Create your views here.

#인원수 뽑아내는 곳
def index(request):
    if request.method  =="POST":
        people = request.POST.get('people')
        return redirect('locations:search', people)
    
    return render(request, 'locations/index.html')



def search(request,people):
    #search 부분 어떻게 받을건지에 따라서 프론트도 백도 많이 달라질 것 같아서 여기서 한번 멈추겠습니다. 
    if request.method == 'POST':
        text = request.POST.get('textinput_1')
        print(text)
        adlist = []        
        for i in range(1, people+1):
            print(request.POST.get(f'textinput_{i}'))
            adlist.append((searchx(request.POST.get(f'textinput_{i}')), searchy(request.POST.get(f'textinput_{i}'))))
        result, position = time(adlist)
        print(position)
        place = json.dumps(position)
        print(place)
        context = {
            'result': result,
            'place' : place,
            'place_name' : adlist,
        }
        return render(request, 'pages/result.html', context)           
    
    else:
        context={
        'people': people
        }
        return render(request, 'locations/search.html', context)

def result(request):
    spot = '' #아마 원래 형식은 둘다 dict이겠지만 spot은 한 곳이고 locations은 복수의 것(사용자 input 값)에 차이를 두기 위해서 이렇게
    #표현해둔거니까 나중에 편하게 바꿔주세요!
    locations = {}
    context = {
        'locations': locations,
        'spot': spot
    }
    return render(request, 'locations/result.html', context)

