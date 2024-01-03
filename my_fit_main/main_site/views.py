from django.shortcuts import render
from django.views.generic import * 

# Create your views here.

def index(request):
    return render(request,"main/index.html")

# 음식 클릭했을 때 디테일 페이지
class FoodListView(DetailView):
    template_name = "main/food_list.html"


class FoodInfoView(DetailView):
    template_name = "main/food_info.html"


class FoodDetailView(DetailView):
    template_name = "main/food_info_detail.html"
