from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,reverse
from django.views.generic import * 
from . models import *

from . forms import * 

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

class ProfileView(DetailView):
    model = User 
    template_name = 'main/profile.html'
    pk_url_kwarg = 'user_id'

    context_object_name = "profile_user"


class ProfileUpdateView(UpdateView):
    model = User 
    form_class = ProfileForm 
    template_name = "main/profile_update_form.html"

    
    def get_object(self,query=None):
        return self.request.user 
    
    def get_success_url(self):
        return reverse("profile",kwargs=({"user_id":self.request.user.id}))



## 장고 2가지 , 1 . FBV (함수형 뷰) , CBV (클래스형 뷰)
# def profile(requests): (함수형 뷰)
# 함수형 def urls에 갔을 떄, path('..../',profile.views(),name='')
# 클래스형 class ~~View(ListView,DetailView) , path('...../',views.ProfileView.as_views())
    
