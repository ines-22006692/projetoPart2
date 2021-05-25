from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .matplot import comentariosGraficoCircular, comentariosGraficoBarras, quizzPessoal, quizzGrupo
from .forms import ContactoForm, ComentarioForm, QuizzForm

# Create your views here.
from .models import Contacto

# Create your views here.
def home_page_view(request):

    return render(request, 'website/home.html')

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

def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        quizz = form.save()
        return HttpResponseRedirect(reverse('website:quizzResultados', args=(quizz.id,)))

    context = {
        'form': form,
    }
    return render(request, 'website/quizz.html', context)


def comentario_page_view(request):
    return render(request, 'website/comentario.html')

def contactoLista_page_view(request):
    context = {'contactos': sorted(Contacto.objects.all(), key=lambda objeto: objeto.id)}
    return render(request, 'website/contactoLista.html', context)

def contactoApaga_page_view(request, contacto_id):
    Contacto.objects.get(pk=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:home'))

def contactoEditar_page_view(request, contacto_id):
    contacto = Contacto.objects.get(pk=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form, 'contacto_id': contacto_id}

    return render(request, 'website/contactoEditar.html', context)

def contacto_page_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {
        'form': form,
        #'contactos': Contacto.objects.all(),
    }
    return render(request, 'website/contacto.html')

def quizzResultado_page_view(request, id):
    context = {
        'graficoPessoal': quizzPessoal(id),
        'graficoGrupo': quizzGrupo(id),
    }
    return render(request, 'website/quizzResultados.html', context)