from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),  # para quando abrir a app o default seja esta
    path('home', views.quizz_page_view, name='quizz'),
    path('page1', views.comentario_page_view, name='comentario'),
    path('page2', views.contacto_page_view, name='contacto')
]