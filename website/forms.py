from django import forms
from django.forms import ModelForm
from .models import Contacto, Comentario, Quizz, Pessoa

#por rever
class ContactoForm(ModelForm):
    formatacao = ["%d/%m/%Y"]
    dataNascimento = forms.DateField(input_formats=formatacao, label="Data de Nascimento")

    class Meta:
        model = Contacto
        fields = '__all__'

#feito
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
            'campo1': "O site encontra-se explicíto relativamente ao assunto que é tratado?",
            'campo2': "Avaliação no design (sendo 1 o pior e 5 o melhor):",
            'campo3': "Como classifica o nosso website quanto à Clareza?",
            'campo4': "Como classifica o nosso website quanto à precisão?",
            'campo5': "Avaliação na originalidade (sendo 1 o pior e 5 o melhor):",
            'campo6': " Como classifica o nosso website quanto ao rigor (0 a 100)?",
            'campo7': "Como classifica o nosso website quanto à profundidade?",
            'campo8': " Qual a percentagem de facilidade de navegação nas várias páginas do web site??",
            'campo9': "Sugestões de Melhoria:"
        }

#feito
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
            'p4': forms.RadioSelect(choices=quantidade),
            'p5': forms.RadioSelect(choices=quantidade),
            'p6': forms.RadioSelect(choices=quantidade),
            'p7': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'p8': forms.RadioSelect(choices=quantidade),
            'pontos': forms.HiddenInput(),
        }
        labels = {
            'p1': "Em que país é localizado Moscovo? ",
            'p2': "Em que país é localizado Lofoten? ",
            'p3': "Em que país é localizado Vancouver? ",
            'p4': "Quantas linguas se fala em Vancouver? ",
            'p5': "Qual é o número de habitantes estimados em Moscovo?",
            'p6': "Qual é aproximadamente a área da cidade de Lofoten?",
            'p7': "Quando é que foi fundado a cidade de Moscovo?",
            'p8': "É verdade que a cidade de Lofoten pertence à União Europeia?",
            'p9': "Vancouver situa-se na America do Sul?",
            'p10': "Quanto é que acha que vai ter neste Quizz (0 a 20)?",
        }
