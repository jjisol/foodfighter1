from django.shortcuts import render
from .models import Foods

def food_list(request):
    return render(request, 'food/index.html', {})# Create your views here.

def korean_food_list(request):
    foods = Foods.objects.filter(title__icontains="한식")
    return render(request, 'food/map.html', {'foods':foods})

def chinese_food_list(request):
    foods = Foods.objects.filter(title__icontains="중식")
    return render(request, 'food/map.html', {'foods':foods})

def japanese_food_list(request):
    foods = Foods.objects.filter(title__icontains="일식")
    return render(request, 'food/map.html', {'foods':foods})

def western_food_list(request):
    foods = Foods.objects.filter(title__icontains="양식")
    return render(request, 'food/map.html', {'foods':foods})

def etc_food_list(request):
    foods = Foods.objects.filter(title__icontains="기타")
    return render(request, 'food/map.html', {'foods':foods})
