from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.

#인원수 뽑아내는 곳
def index(request):
    if request.method  =="POST":
        people = request.POST.get('people')
        return redirect('locations:search', people)
    
    return render(request, 'locations/index.html')



def search(request,people):
    #search 부분 어떻게 받을건지에 따라서 프론트도 백도 많이 달라질 것 같아서 여기서 한번 멈추겠습니다. 
    if request.method =="POST":
        pass
    else:
        #일단 인원수 만큼 form 뽑아뒀는데 id가 다 같아서 그부분은 좀 고민을 해봐야할 것 같고 백엔드쪽이 편한 대로 바꿀 수 있으니까 
        #해보고 알려주세요
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


def addressresult(request):
    return render(request, 'locations/addressresult.html')
