from django.contrib import admin
from .models import Contacto, Comentario, Quizz, Pessoa


# Register your models here.

admin.site.register(Quizz)
admin.site.register(Comentario)
admin.site.register(Pessoa)
admin.site.register(Contacto)
