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
    #검색버튼 submit 후 mypath 모듈 이용해 해당 스팟 찾아내고 result 페이지로 넘겨주기
    if request.method == 'POST':
        adlist = []
        placename_list = []        
        for i in range(1, people+1):
            text = request.POST.get(f'textinput_{i}')
            placename_list.append(text)
            adlist.append((searchx(text), searchy(text)))
        result, place, position = time(adlist)
        context = {
            'result': int(result)//people,
            'place' : place,
            'position_x':position[0],
            'position_y': position[1],
            'placename_list': placename_list,
        }
        return render(request, 'locations/result.html', context)           
    #인원별 주소지 검색 
    else:
        context={
        'people': people
        }
        return render(request, 'locations/search.html', context)



