from django.db import models


# Create your models here.

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, default="", verbose_name="Your name: ")
    email = models.EmailField()
    telefone = models.CharField(max_length=18, blank=True)
    dataCriacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    explicito = models.CharField(max_length=30, default="",verbose_name="O site encontra-se explicíto relativamente ao assunto que é tratado? ")
    clareza = models.CharField(max_length=10, default=3)
    precisao = models.CharField(max_length=10, default=3)
    originalidade = models.CharField(max_length=10, default=3)
    design = models.IntegerField(default=3, verbose_name="Avaliação no design (sendo 1 o pior e 5 o melhor)")
    rigor = models.IntegerField(default=3, verbose_name="Avaliação no rigor (sendo 1 o pior e 5 o melhor)")
    amplitude = models.IntegerField(default=50,verbose_name="Como classifica o nosso website quanto à amplitude (0 a 100)?")
    profundidade = models.IntegerField(default=50,verbose_name="Como classifica o nosso website quanto à profundidade (0 a 100)?")
    navegacao = models.IntegerField(default=50,verbose_name="Qual a percentagem de facilidade de navegação nas várias páginas do web site? ")
    feedBack = models.TextField(default="")

    def __str__(self):
            return str(self.id)

class Quizz(models.Model):
    id = models.AutoField(primary_key=True)
    pontos = models.IntegerField(default=0)
    nome = models.CharField(max_length=30, default="", verbose_name="Your name: ")
    p1 = models.CharField(max_length=40, default="")
    p2 = models.CharField(max_length=40, default="")
    p3 = models.CharField(max_length=40, default="")
    quantidade = [
        ("Sim", "Sim"),
        ("Não", "Não"),
    ]
    p4 = models.CharField(choices=quantidade, default="", max_length=40)
    opcoes = [
        ("20,02", "20,02"),
        ("11,92", "11,92"),
        ("10,82", "10,82"),
    ]
    p5 = models.CharField(choices=opcoes, default="", max_length=40)
    p6 = models.IntegerField(default=0)
    p7 = models.IntegerField(default=0)
    p8 = models.IntegerField(default=0)
    p9 = models.CharField(max_length=40, default="")
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
        (10, 10)
    ]
    p10 = models.IntegerField(default=0, choices=opcoesNota)

    def __str__(self):
        return str(self.id)


class Pessoa(models.Model):
    nome = models.CharField(max_length=30, default="", verbose_name="O seu Nome ")
    contacto = models.ForeignKey(Contacto, on_delete=models.SET_NULL, blank=True, null=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.SET_NULL, blank=True, null=True)
    quizz = models.ForeignKey(Quizz, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome
