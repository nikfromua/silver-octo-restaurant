from django.shortcuts import render
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

class TodayMenuView(APIView):
    def get(self, request, *args, **kwargs):
        today = date.today()
        menus = Menu.objects.filter(date=today)
        serialized_menus = MenuSerializer(menus, many=True)
        return Response(serialized_menus.data)
