from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name=''),  # para quando abrir a app o default seja esta
    path('home', views.home_page_view, name='home'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('comentario', views.comentario_page_view, name='comentario'),
    path('atividadeLofoten', views.atividade_lofoten_view, name='atividadeLofoten'),
    path('atividadeMoscovo', views.atividade_moscovo_view, name='atividadeMoscovo'),
    path('atividadeVancover', views.atividade_vancover_view, name='atividadeVancover'),
    path('estiloPagina', views.estio_page_view, name='estiloPagina'),
    path('ida_e_volaLofoten', views.ida_e_voltaLofoten_view, name='ida_e_voltaLofoten'),
    path('ida_e_voltaVancover', views.ida_e_voltaVancover_view, name='ida_e_voltaVancover'),
    path('ida_e_voltaMoscovo', views.ida_e_voltaMoscovo_view, name='ida_e_voltaMoscovo'),
    path('imagensLofoten', views.imagens_lofoten_view, name='imagensLofoten'),
    path('imagensVancover', views.imagens_vancover_view, name='imagensVancover'),
    path('imagensMoscovo', views.imagens_moscovo_view, name='imagensMosvovo'),
    path('informacaoLofoten', views.informacao_lofoten_view, name='informacaoLofoten'),
    path('informacaoVancover', views.informacao_vancover_view, name='informacaoVancover'),
    path('informacaoMoscovo', views.informacao_moscovo_view, name='informacaoMoscover'),
    path('marcarViagemLofoten', views.marcar_lofoten_view, name='marcarViagemLofoten'),
    path('marcarViagemVancover', views.marcar_vancover_view, name='marcarViagemVancover'),
    path('marcarViagemMoscovo', views.marcar_moscovo_view, name='marcarViagemMoscovo'),
    path('quizzResult/<int:id>', views.quizzResult_page_view, name='quizzResult'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('ListaContactos', views.contactoLista_page_view, name='contactoLista'),
    path('editar/<int:contacto_id>', views.contactoEditar_page_view, name='contactoEdita'),
    path('apagar/<int:contacto_id>', views.contactoApaga_page_view, name='contactoApaga'),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
]
