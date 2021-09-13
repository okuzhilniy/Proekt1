from django.urls import path
from . import views

urlpatterns = [
    path('', views.osnova, name='osnova'),
    path('Блог', views.Блог, name='Блог'),
    path('Магазин', views.Магазин, name='Магазин'),
    path('Контакты', views.Контакты, name='Контакты'),
    path('Кабинет', views.Кабинет, name='Кабинет'),
]