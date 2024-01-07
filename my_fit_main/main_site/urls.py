from django.urls import path
from . import views
from .models import * 
from .views import FoodDetailView, FoodInfoView, FoodListView

urlpatterns = [
    path('',views.index,name="index"),

    ## 디테일 페이지
    # views,{views.py에서 만들어놓은 class명}.as_views()
    # 음식리스트(카테고리별)
    path('food_list/',views.FoodListView.as_view(), name='food_list'),
    # 음식정보
    path('food_info/<int:pk>/',views.FoodInfoView.as_view(), name='food_info'),
    # 음식 상세페이지
    path('food_info_detail/<int:food_id>/',views.FoodDetailView.as_view(), name='food_info_detail'),

    # 회원 프로필 
    path('users/<int:user_id>/',views.ProfileView.as_view(),name='profile'),
]
