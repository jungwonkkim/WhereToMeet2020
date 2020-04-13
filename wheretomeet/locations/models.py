from django.db import models

# Create your models here.
# class Location(models.Model):
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     lo_id = models.CharField(max_length = 16)
#     name = models.CharField(max_length= 30)


# class Powerspot(models.Model):
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     ps_id = models.CharField(max_length = 16)
#     name = models.CharField(max_length = 30)

# 아까 이야기 했던 것처럼 우린 이걸 데이터베이스에 영원히 가지고 있을 필요가 없어서 이게 굳이 필요한가 싶습니다. 
# 이 부분은 아까 다 동의하긴 했는데 후에 알고리즘 돌릴 때 완전 필요할 것 같기도 함 내 머리로는 아직 한번에 폼 여러 개 받을 때 
# CRUD나 모달폼 이용안하고는 방법을 모르겠음\