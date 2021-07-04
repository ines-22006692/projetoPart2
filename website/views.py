import time
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .matplot import comentGrafC,respostaQuiz
from .forms import ContactoForm, ComentarioForm, QuizzForm

from .models import Contacto, Pessoa


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
    return render(request, 'website/atividadeVancouver.html')

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
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        questionario = form.save()
        Pessoa.objects.get_or_create(nome=questionario.nome)
        peopl = Pessoa.objects.get(nome=questionario.nome)
        peopl.quizz = questionario
        peopl.save()
        return HttpResponseRedirect(reverse('website:quizzResultado', args=(questionario.id,)))

    context = {
        'form': form,
    }
    return render(request, 'website/quizz.html', context)

def comentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save()
        Pessoa.objects.get_or_create(nome=comentario.nome)
        pessoa = Pessoa.objects.get(nome=comentario.nome)
        pessoa.comentario = comentario
        pessoa.save()
        context = {
            'form': form,
            'graficoC': comentGrafC()
        }
    else:
        context = {'form': form}

    return render(request, 'website/comentario.html', context)

def contacto_page_view(request):
    forms = ContactoForm(request.POST or None)
    if forms.is_valid():
        contactos = forms.save()
        Pessoa.objects.get_or_create(nome=contactos.nome)
        people = Pessoa.objects.get(nome=contactos.nome)
        people.contactos = contactos
        people.save()
        return HttpResponseRedirect(reverse('website:home'))

    contexts = {'form': forms}

    return render(request, 'website/contacto.html', contexts)

def contactoLista_page_view(request):
    contexts = {'contactos': sorted(Contacto.objects.all(), key=lambda i: i.id)}
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))

    return render(request, 'website/contactoLista.html', contexts)

def contactoEditar_page_view(request, contacto_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))

    contactos = Contacto.objects.get(pk=contacto_id)
    form = ContactoForm(request.POST or None, instance=contactos)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contactoLista'))

    contexts = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/contactoEditar.html', contexts)

def contactoApaga_page_view(request, contacto_id):
    Contacto.objects.get(pk=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:contactoLista'))

def quizzResult_page_view(request, id):
    context = {
        'graphPessoal': respostaQuiz(id),

    }
    return render(request, 'website/quizzResultado.html', context)

def login_view(request):
    if request.method == "POST":
        user = request.POST['username']
        passw = request.POST['password']
        utilizador = authenticate(request, username=user, password=passw)
        if utilizador is not None:
            login(request, utilizador)
            return render(request, 'website/index.html')
        else:
            return render(request, 'website/login.html', {
                'mensagem': "Inválido, tente novamente"
            })
    return render(request, 'website/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'website/index.html')

