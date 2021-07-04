from io import StringIO
from matplotlib import pyplot as plt
from .models import Comentario, Quizz

def respostaQuiz(quizz_id):

    aswers = Quizz.objects.get(id=quizz_id)
    n_perguntas = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
    listChav = []
    point=0
    if aswers.p1 == "Rússia":
        point += 1
        lista_chav.append(1)
    elif aswers.p1 == "Russia":
        point += 0.5
        lista_chav.append(0.5)
    elif aswers.p1 == "russia":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    if aswers.p2 == "Noruega":
        point += 1
        lista_chav.append(1)
    elif str(aswers.p1) == "noruega":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    if aswers.p3 == "Canadá":
        point += 1
        lista_chav.append(1)
    elif aswers.p3 == "Canada":
        point += 0.5
        lista_chav.append(0.5)
    elif aswers.p3 == "canada":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    if aswers.p4 == "Não":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if aswers.p5 == "11,92":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if str(aswers.p6) == "1227":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if str(aswers.p7) == "1147":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if str(aswers.p8) == "2":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if aswers.p9 == "Não":
        point += 1
        lista_chav.append(1)
    elif aswers.p9 == "Nao":
        point += 0.5
        lista_chav.append(0.5)
    elif aswers.p9 == "não":
        point += 1
        lista_chav.append(1)
    elif aswers.p9 == "nao":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    # p10
    point += 1
    lista_chav.append(1)

    aswers.point = point
    aswers.save()


    fig = plt.figure()
    plt.bar(listaKeys, listChav)
    plt.title("Gráfico Critérios Considerados")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def comentGrafC():
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

def questionario(quizz_id):
    quest = Quizz.objects.get(id=quizz_id)
    n_perguntas = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
    lista_chav = []
    point = 0.0
    if quest.p1 == "Rússia":
        point += 1
        lista_chav.append(1)
    elif quest.p1 == "Russia":
        point += 0.5
        lista_chav.append(0.5)
    elif quest.p1 == "russia":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    if quest.p2 == "Noruega":
        point += 1
        lista_chav.append(1)
    elif str(quest.p1) == "noruega":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    if quest.p3 == "Canadá":
        point += 1
        lista_chav.append(1)
    elif quest.p3 == "Canada":
        point += 0.5
        lista_chav.append(0.5)
    elif quest.p3 == "canada":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    if quest.p4 == "Não":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if quest.p5 == "11,92":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if str(quest.p6) == "1227":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if str(quest.p7) == "1147":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if str(quest.p8) == "2":
        point += 1
        lista_chav.append(1)
    else:
        lista_chav.append(0)

    if quest.p9 == "Não":
        point += 1
        lista_chav.append(1)
    elif quest.p9 == "Nao":
        point += 0.5
        lista_chav.append(0.5)
    elif quest.p9 == "não":
        point += 1
        lista_chav.append(1)
    elif quest.p9 == "nao":
        point += 0.5
        lista_chav.append(0.5)
    else:
        lista_chav.append(0)

    # p10
    point += 1
    lista_chav.append(1)
    quest.point = point
    quest.save()
    figura = plt.figure()
    plt.barh(n_perguntas, lista_chav)
    plt.title(f"Gráfico das questões\n"
              f"Pontos {quest.point} em 10")
    figura.set_facecolor((0.921, 0.921, 0.921))
    figura.set_size_inches(10, 10)
    imagemdate = StringIO()
    figura.savefig(imagemdate, format='svg')
    imagemdate.seek(0)
    date = imagemdate.getvalue()
    return date

def quizzMedia(quizz_id):
    questionary = Quizz.objects.all()
    actualList = Quizz.objects.get(id=quizz_id)
    pontuacao = ["Pontuação Média", "Sua Pontuação"]
    lista_chave = []
    media = 0.0
    usadores = 0.0
    for i in questionary:
        media += i.pontos
        usadores += 1

    media = media / usadores
    lista_chave.append(media)
    lista_chave.append(actualList.pontos)

    figura = plt.figure()
    plt.bar(pontuacao, lista_chave)
    plt.title("Gráfico Comparação")
    figura.set_facecolor((0.921, 0.921, 0.921))
    figura.set_size_inches(3, 5)

    imagemdate = StringIO()
    figura.savefig(imagemdate, format='svg')
    imagemdate.seek(0)
    date = imagemdate.getvalue()
    return date
