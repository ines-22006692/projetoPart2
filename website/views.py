from django.shortcuts import render
import datetime


# Create your views here.
def home_page_view(request):

    return render(request, 'website/index.html')

def estio_page_view(request):
    return render(request, 'website/estiloPagina.html')

def atividade_lofoten_view(request):
    return render(request, 'website/atividadeLofoten.html')

def atividade_moscovo_view(request):
    return render(request, 'website/atividadeMoscovo.html')

def atividade_vancover_view(request):
    return render(request, 'website/atividadeVancover.html')

def ida_e_voltaLofoten_view(request):
    return render(request, 'website/ida_e_voltaLofoten.html')

def ida_e_voltaMoscovo_view(request):
    return render(request, 'website/ida_e_voltaMoscovo.html')

def ida_e_voltaVancover_view(request):
    return render(request, 'website/ida_e_voltaVancover.html')

def imagens_lofoten_view(request):
    return render(request, 'website/imagensLofoten.html')

def imagens_vancover_view(request):
    return render(request, 'website/imagensVancover.html')

def imagens_moscovo_view(request):
    return render(request, 'website/imagensMoscovo.html')

def imagens_lofoten_view(request):
    return render(request, 'website/imagensLofoten.html')

def informacao_lofoten_view(request):
    return render(request, 'website/informacaoLofoten.html')

def informacao_vancover_view(request):
    return render(request, 'website/informacaoVancover.html')

def informacao_moscovo_view(request):
    return render(request, 'website/informacaoMoscovo.html')

def marcar_vancover_view(request):
    return render(request, 'website/marcarViagemVancover.html')

def marcar_lofoten_view(request):
    return render(request, 'website/marcarViagemLofoten.html')

def marcar_moscovo_view(request):
    return render(request, 'website/marcarViagemMoscovo.html')

def marcar_vancover_view(request):
    return render(request, 'website/marcarViagemVancover.html')

def marcar_lofoten_view(request):
    return render(request, 'website/marcarViagemLofoten.html')

def marcar_moscovo_view(request):
    return render(request, 'website/marcarViagemMoscovo.html')

def quizz_page_view(request):
    return render(request, 'website/quizz.html')


def comentario_page_view(request):
    return render(request, 'website/comentario.html')



