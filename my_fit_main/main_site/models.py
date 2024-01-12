from django.db import models
from django.contrib.auth.models import AbstractUser # 회원가입 모델 
from django.contrib.auth.models import User


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=15,unique=True,null=True,
                                error_messages={'unique':'이미 사용중인 닉네임'},
                                ) # 최대 길이 15자, 유일성 유지 
    
    profile_pic = models.ImageField(default="default_profile_pic.jpg",
                                    upload_to="profile_pics",
                                    blank=True) # 프로필 사진 안 올리면 기본 사진으로

    intro = models.CharField(max_length=60,blank=True) # 자기소개

class Profile(models.Model):
    intro = models.CharField(max_length=60, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nickname


class Food(models.Model):
    name = models.CharField(max_length=100)
    food_image = models.ImageField(upload_to='food_pics')

    calories = models.FloatField()  # 칼로리
    carbohydrates = models.FloatField()  # 탄수화물
    protein = models.FloatField()   # 단백질
    fat = models.FloatField()       # 지방
    iron = models.FloatField(default=0.0, null=True)  # 철
    dietary_fiber = models.FloatField(default=0.0, null=True)  # 식이섬유
    vitamin_c = models.FloatField(default=0.0, null=True)  # 비타민 C
    vitamin_b1 = models.FloatField(default=0.0, null=True)  # 비타민 B1
    vitamin_b2 = models.FloatField(default=0.0, null=True)  # 비타민 B2
    sodium = models.FloatField(default=0.0, null=True)  # 나트륨
    calcium = models.FloatField(default=0.0, null=True)  # 칼슘
    saturated_fat = models.FloatField(default=0.0, null=True)  # 포화지방산
    trans_fat = models.FloatField(default=0.0, null=True)  # 트랜스지방산
    

    def __str__(self):
        return self.name

