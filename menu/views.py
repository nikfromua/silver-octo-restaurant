from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Страва

def list_of_dishes(request):
    dishes = Страва.objects.all()
    return render(request, 'menu/list_of_dishes.html', {'dishes': dishes})

def dish_details(request, dish_id):
    dish = get_object_or_404(Страва, id=dish_id)
    return render(request, 'menu/dish_details.html', {'dish': dish})

def home(request):
    return render(request, "home.html")

