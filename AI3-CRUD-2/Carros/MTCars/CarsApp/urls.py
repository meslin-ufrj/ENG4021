from django.contrib import admin
from django.urls import path
from CarsApp import views

app_name = "CarsApp"

urlpatterns = [
    path("", views.searchf, name="home"),
    # o nome carro_id é usado para capturar o ID do carro na URL
    # ele tem que ser o mesmo nome que está na função detalhes() em views.py
    path("detalhes/<int:carro_id>/", views.detalhes, name="detalhes"),
]
