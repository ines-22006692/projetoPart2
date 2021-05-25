from django.shortcuts import render
import datetime


# Create your views here.
def home_page_view(request):

    return render(request, 'website/home.html')



def quizz_page_view(request):

    return render(request, 'website/quizz.html')


def comentario_page_view(request):
    return render(request, 'website/comentario.html')


def contacto_page_view(request):
    return render(request, 'website/contacto.html')