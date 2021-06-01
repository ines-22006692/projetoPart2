from django.db import models


# Create your models here.

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    email = models.EmailField()
    telefone = models.CharField(max_length=17, blank=True)
    dataNascimento = models.DateField()
    dataCriacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default="", verbose_name="Your name: ")
    campo1 = models.BooleanField(verbose_name="O site encontra-se explicíto relativamente ao assunto que é tratado?", default=False)
    campo2 = models.CharField(max_length=10, default=3)
    campo3 = models.CharField(max_length=10, default=3)
    campo4 = models.CharField(max_length=10, default=3)
    campo5 = models.CharField(max_length=10, default=3)
    campo6 = models.CharField(max_length=10, default=3)
    campo7 = models.CharField(max_length=10, default=3)
    campo8 = models.CharField(max_length=10, default=3)
    campo9 = models.CharField(max_length=10, default=3)
    def __str__(self):
        return str(self.id)

#Rever
class Quizz(models.Model):
    quantidade = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    id = models.AutoField(primary_key=True)
    pontos = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default="", verbose_name="Your name: ")
    p1 = models.IntegerField(default=0)
    p2 = models.CharField(max_length=40, default="")
    p3 = models.CharField(max_length=40, default="")
    p4 = models.IntegerField(choices=quantidade, default=0)
    opcoes4 = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    ]
    p5 = models.IntegerField(choices=quantidade, default=0)
    opcoes5 = [
        ("11,92", "11,92"),
        ("11,10", "11,10"),
        ("12,00", "12,00"),
    ]
    p6 = models.IntegerField(choices=quantidade, default=0)
    opcoes6 = [
        ("1215", "1215"),
        ("1421", "1421"),
        ("1227", "1227"),
    ]
    #falta fazer o p7 por causa da data
    p7 = models.CharField(max_length=40, default="")
    p8 = models.BooleanField(verbose_name="Vancouver situa-se na America do Sul?", default=False)
    p9 = models.IntegerField(default=0, choices=quantidade)
    opcoesNota = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
    ]
    p10 = models.IntegerField(default=0, choices=opcoesNota)

    def __str__(self):
        return str(self.id)


# REQUISITO DA FOREIGN KEY
class Pessoa(models.Model):
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    contacto = models.ForeignKey(Contacto, on_delete=models.SET_NULL, blank=True, null=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.SET_NULL, blank=True, null=True)
    quizz = models.ForeignKey(Quizz, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome
