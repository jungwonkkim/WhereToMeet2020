from django.urls import path
from . import views

app_name = "locations"

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('<int:people>/', views.search, name='search'),
    path('addressresult/', views.addressresult, name='addressresult')
]