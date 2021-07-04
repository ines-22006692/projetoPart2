from django import forms
from django.forms import ModelForm
from .models import Contacto, Comentario, Quizz, Pessoa


class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        op = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'clareza': forms.RadioSelect(choices=op),
            'originalidade': forms.RadioSelect(choices=op),
            'precisao': forms.RadioSelect(choices=op),
        }

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        op = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'p8': forms.RadioSelect(choices=op),
            'pontos': forms.HiddenInput(),
        }
        labels = {
            'p1': "Em que país é localizado Moscovo? ",
            'p2': "Em que país é localizado Lofoten? ",
            'p3': "Em que país é localizado Vancouver? ",
            'p4': "É verdade que a cidade de Lofoten pertence à União Europeia?",
            'p5': "Qual é o número de habitantes estimados em Moscovo?",
            'p6': "Qual é aproximadamente a área da cidade de Lofoten?",
            'p7': "Em que ano foi fundado a cidade de Moscovo?",
            'p8': "Quantas linguas se fala em Vancouver? ",
            'p9': "Vancouver situa-se na America do Sul?",
            'p10': "Quanto é que acha que vai ter neste Quizz (0 a 10)?",
        }
