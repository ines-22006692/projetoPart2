# PAGINA ONDE FAZ OS GRAFICOS MATPLOTLIB
from io import StringIO

from matplotlib import pyplot as plt

from .models import Comentario, Quizz



def comentariosGraficoCircular():
    comentarios = Comentario.objects.all()
    listaKeys = ['Originalidade', 'Clareza', 'Precisao']
    originalidade = 0
    clareza = 0
    precisao = 0
    listaValues = []
    for coment in comentarios:
        originalidade += int(coment.rigor)
        clareza += int(coment.clareza)
        precisao += int(coment.precisao)
    listaValues.append(originalidade)
    listaValues.append(clareza)
    listaValues.append(precisao)

    fig = plt.figure()
    plt.pie(listaValues, labels=listaKeys, autopct='%1.0f%%')
    plt.title("Gráfico Critérios de Avaliação")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def comentariosGraficoBarras():
    comentarios = Comentario.objects.all()
    listaKeys = ['Rigor', 'Design', 'Naveg', 'Prof']
    rigor = 0
    design = 0
    navegacao = 0
    profundidade = 0
    listaValues = []
    for coment in comentarios:
        if coment.rigor:
            rigor += 1
        if coment.design:
            design += 1
        if coment.navegacao:
            navegacao += 1
        if coment.profundidade:
            profundidade += 1
    listaValues.append(rigor)
    listaValues.append(design)
    listaValues.append(navegacao)
    listaValues.append(profundidade)

    fig = plt.figure()
    plt.bar(listaKeys, listaValues)
    plt.title("Gráfico Critérios Considerados")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data



def quizzPessoal(quizz_id):
    quizz = Quizz.objects.get(id=quizz_id)
    listaKeys = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
    listaValues = []
    pontos = 0.0
    if quizz.p1 == "Rússia":
        pontos += 1
        listaValues.append(1)
    elif quizz.p1 == "Russia":
        pontos += 0.5
        listaValues.append(0.5)
    elif quizz.p1 == "russia":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if quizz.p2 == "Noruega":
        pontos += 1
        listaValues.append(1)
    elif str(quizz.p1) == "noruega":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if quizz.p3 == "Canadá":
        pontos += 1
        listaValues.append(1)
    elif quizz.p3 == "Canada":
        pontos += 0.5
        listaValues.append(0.5)
    elif quizz.p3 == "canada":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    if quizz.p4 == "Não":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if quizz.p5 == "11,92":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if str(quizz.p6) == "1227":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if str(quizz.p7) == "1147":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if str(quizz.p8) == "2":
        pontos += 1
        listaValues.append(1)
    else:
        listaValues.append(0)

    if  quizz.p9 == "Não":
        pontos += 1
        listaValues.append(1)
    elif quizz.p9 == "Nao":
        pontos += 0.5
        listaValues.append(0.5)
    elif quizz.p9 == "não":
        pontos += 1
        listaValues.append(1)
    elif quizz.p9 == "nao":
        pontos += 0.5
        listaValues.append(0.5)
    else:
        listaValues.append(0)

    # p10
    pontos += 1
    listaValues.append(1)

    # grava pontos na base de dados
    quizz.pontos = pontos
    quizz.save()

    fig = plt.figure()
    plt.barh(listaKeys, listaValues)
    plt.title(f"Gráfico Pontos Por Perguntas\n"
              f"Total {quizz.pontos} em 10")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(5, 5)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def quizzGrupo(quizz_id):
    quizzes = Quizz.objects.all()
    quizzAtual = Quizz.objects.get(id=quizz_id)
    listaKeys = ["Pontuação Média", "Sua Pontuação"]
    listaValues = []
    mediaGeral = 0.0
    totalUsers = 0.0
    for quizz in quizzes:
        mediaGeral += quizz.pontos
        totalUsers += 1

    mediaGeral = mediaGeral / totalUsers
    listaValues.append(mediaGeral)
    listaValues.append(quizzAtual.pontos)

    fig = plt.figure()
    plt.bar(listaKeys, listaValues)
    plt.title("Gráfico Comparação")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(3, 5)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data
