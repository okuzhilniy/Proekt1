from django.shortcuts import render
from django.http import HttpResponse


def osnova(request):
    return render(request, 'main/osnova.html')


def Блог(request):
    return render(request, 'main/Блог.html')


def Магазин(request):
    return render(request, 'main/Магазин.html')


def Контакты(request):
    return render(request, 'main/Контакты.html')


def Кабинет(request):
    return render(request, 'main/Кабинет.html')
