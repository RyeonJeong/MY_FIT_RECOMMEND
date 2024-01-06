from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import * 
from . models import *

# Create your views here.

def index(request):
    return render(request,"main/index.html")

# 음식 클릭했을 때 디테일 페이지
class FoodListView(ListView):
    model = Food
    template_name = 'main/food_list.html'
    
    paginate_by = 4 
    context_object_name = 'food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.all() # 모든 음식정보 갖고오기
        return context


class FoodInfoView(ListView):
    model = Food
    template_name = 'main/food_info.html'
    pk_url_kwarg = 'food'

    
class FoodDetailView(DetailView):
    model = Food 
    template_name = "main/food_info_detail.html"
    pk_url_kwarg = 'food_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food_list"] = Food.objects.all()
        return context
