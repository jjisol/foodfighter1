from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('korean/food/list', views.korean_food_list, name='korean_food_list'),
    path('chinese/food/list', views.chinese_food_list, name='chinese_food_list'),
    path('japanese/food/list', views.japanese_food_list, name='japanese_food_list'),
    path('western/food/list', views.western_food_list, name='western_food_list'),
    path('etc/food/list', views.etc_food_list, name='etc_food_list'),
]
