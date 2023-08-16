from django.shortcuts import render, get_object_or_404
from .models import Страва
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vote, Menu  # імпортуйте інші моделі, якщо потрібно
from datetime import date

def list_of_dishes(request):
    dishes = Страва.objects.all()
    return render(request, 'menu/list_of_dishes.html', {'dishes': dishes})

def dish_details(request, dish_id):
    dish = get_object_or_404(Страва, id=dish_id)
    return render(request, 'menu/dish_details.html', {'dish': dish})

def home(request):
    return render(request, "home.html")

class VoteMenuView(APIView):
    def post(self, request, *args, **kwargs):
        menu_id = request.data.get("menu_id")
        employee = request.user  # Припустимо, що співробітник аутентифікований
        vote, created = Vote.objects.get_or_create(menu_id=menu_id, employee=employee, date=date.today())
        if created:
            return Response({"message": "Vote recorded!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You've already voted today!"}, status=status.HTTP_400_BAD_REQUEST)

class VotingResultsView(APIView):
    def get(self, request, *args, **kwargs):
        today_votes = Vote.objects.filter(date=date.today())
        # Тут можна додати логіку підрахунку голосів для кожного меню
        # Наприклад, використовуючи Django ORM's annotate і Count
        # Або просто перебрати все в циклі

