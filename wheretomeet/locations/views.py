from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.

#인원수 뽑아내는 곳
def index(request):
    if request.method  =="POST":
        people = request.POST.get('people')
        return redirect('locations:search', people)
    else:
        return render(request, 'locations/index.html')



def search(request,people):
    #search 부분 어떻게 받을건지에 따라서 프론트도 백도 많이 달라질 것 같아서 여기서 한번 멈추겠습니다. 
    if request.method =="POST":
        location_x = 0
        location_y = 0
        location_x += request.POST.get('location.x') 
        location_y += request.POST.get('location.y') 
        #지금 경로시간이 API에서 안잡혀서 일단은 위도 경도만 뽑을까 생각중이에요(내가 결정할 부분 아니니까 이건 두분이서 잘 상의해보세용)
        #이 밑에 자유롭게 번화가 찾는 알고리즘 작성하시면 될 것 같아요 그냥 spot들도 
        # 개인적으로는 여기에 json으로 그냥 위도 경도 이름 id 
        # 여기서 그냥 선언해버리고 써도 될듯 
        # 처리할 것 다 하셨다면 result 로 위/경도/위치id/위치명 있는 json 내지 dict 필요합니다!
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
    #각각의 주소찾아서 찾으려고 하는 주소를 넣고 빼는 거 하려고 하는데 이것도 마찬가지고 목록 빼는게 Rest API 사용
    #하는 부분이라 그 부분 부탁드릴게요. 그런데 이 부분(과 search) Modal로 표현할 지 아니면 새 창으로 표현할지 고민중이에요
    #그래서 아직 html 안 만듬.
    #그 부분은 js/html/css로 ㅁ지는 부분이니까 조금 더 고민해볼게요 특히 Modal로 하게 되면 js가 많이 움직여야 할 것 같아요
    pass