from django import forms
from django.forms import ModelForm
from .models import Contacto, Comentario, Quizz


class ContactoForm(ModelForm):
    formatacao = ["%d/%m/%Y"]
    dataNascimento = forms.DateField(input_formats = formatacao)
    class Meta:
        model = Contacto
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        opcoes = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'campo4': forms.RadioSelect(choices=opcoes),
            'campo5': forms.RadioSelect(choices=opcoes),
            'rigor': forms.RadioSelect(choices=opcoes),
            'precisao': forms.RadioSelect(choices=opcoes),
        }
        labels = {
            'campo1': "Nome",
            'campo2': "O site encontra-se explicíto relativamente ao assunto que é tratado?",
            'campo3': "Avaliação no design (sendo 1 o pior e 5 o melhor):",
            'campo4': "Como classifica o nosso website quanto à Clareza?",
            'campo5': "Como classifica o nosso website quanto à precisão?",
            'campo6': "Avaliação na originalidade (sendo 1 o pior e 5 o melhor):",
            'campo7': " Como classifica o nosso website quanto ao rigor (0 a 100)?",
            'campo8': "Como classifica o nosso website quanto à profundidade?",
            'campo9': " Qual a percentagem de facilidade de navegação nas várias páginas do web site??",
            'campo10': "Sugestões de Melhoria:"
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        quantidade = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'p1': forms.RadioSelect(choices=quantidade),
            'p2': forms.RadioSelect(choices=quantidade),
            'p3': forms.RadioSelect(choices=quantidade),
            'p7': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'pontos': forms.HiddenInput(),
        }
        labels = {
            'nome': "Nome ",
            'apelido': "Apelido  ",
            'p1': "Em que continente é localizado Moscovo? ",
            'p2': "Em que continente é localizado Lofeton? ",
            'p3': "Em que continente é localizado Vancover? ",
            'p4': "Quantas linguas se fala em Vancover? ",
            'p5': "Qual é o número de habitantes estimados em Moscovo?",
            'p6': "Qual é aproximadamente a área da cidade de Lofoten?",
            'p7': "Quando é que foi fundado a cidade de Moscovo?",
            'p8': "",
            'p9': "",
            'p10': "Quanto é que acha que vai ter neste Quizz (0 a 20)?",
        }