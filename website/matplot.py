from io import StringIO
from matplotlib import pyplot as plt
from .models import Comentario, Quizz
def respostaQuiz(quizz_id):
    questionary = Quizz.objects.all()
    aswers = Quizz.objects.get(id=quizz_id)
    n_perguntas = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
    listChav = []
    point=0
    if aswers.p1 == "Rússia":
        point += 1
        listChav.append(1)
    elif aswers.p1 == "Russia":
        point += 0.5
        listChav.append(0.5)
    elif aswers.p1 == "russia":
        point += 0.5
        listChav.append(0.5)
    else:
        listChav.append(0)

    if aswers.p2 == "Noruega":
        point += 1
        listChav.append(1)
    elif str(aswers.p1) == "noruega":
        point += 0.5
        listChav.append(0.5)
    else:
        listChav.append(0)

    if aswers.p3 == "Canadá":
        point += 1
        listChav.append(1)
    elif aswers.p3 == "Canada":
        point += 0.5
        listChav.append(0.5)
    elif aswers.p3 == "canada":
        point += 0.5
        listChav.append(0.5)
    else:
        listChav.append(0)

    if aswers.p4 == "Não":
        point += 1
        listChav.append(1)
    else:
        listChav.append(0)

    if aswers.p5 == "11,92":
        point += 1
        listChav.append(1)
    else:
        listChav.append(0)

    if str(aswers.p6) == "1227":
        point += 1
        listChav.append(1)
    else:
        listChav.append(0)

    if str(aswers.p7) == "1147":
        point += 1
        listChav.append(1)
    else:
        listChav.append(0)

    if str(aswers.p8) == "2":
        point += 1
        listChav.append(1)
    else:
        listChav.append(0)

    if aswers.p9 == "Não":
        point += 1
        listChav.append(1)
    elif aswers.p9 == "Nao":
        point += 0.5
        listChav.append(0.5)
    elif aswers.p9 == "não":
        point += 1
        listChav.append(1)
    elif aswers.p9 == "nao":
        point += 0.5
        listChav.append(0.5)
    else:
        listChav.append(0)

    # p10
    point += 1
    listChav.append(1)

    aswers.point = point
    aswers.save()

    fig = plt.figure()
    plt.bar(n_perguntas, listChav)
    plt.title("Gráfico Critérios Considerados")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 7)

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
