# Preparando o ambiente:
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

#graficos para variaveis qualitativas:
#grafico de barras:

#grafico de setores:
# 1) conjunto de dados:
dados1 = ["Sim"]*20  + ["Nao"]*45
# cria uma especie de dicionario com o counter
respostas1 = Counter(dados1)

'''
#graficos para variaveis qualitativas:
#grafico de barras:

# 2) construcao grafica:
plt.pie(list(respostas1.values()),
        labels=list(respostas1.keys()),
        autopct="%1.2f%%",
        colors=["green",  "red"])
plt.title("Resultado da  Pesquisa Aplicada  pelo McDonalds - 2026")
plt.legend(list(respostas1.keys()),
           loc="upper right",)
plt.show()
'''

'''
# 3) grafico de Barras Verticais:

plt.bar(x=list(respostas1.keys()),
        height=list(respostas1.values()),
        color=["blue","red"])
plt.title("Resultado da  Pesquisa Aplicada  pelo McDonalds - 2026")
plt.legend(list(respostas1.keys()),
           loc="upper right",)
#mostrar  o  grafico
plt.show()
'''

'''
#grafico de Barras Horizontal:

plt.barh(y=list(respostas1.keys()),
        width=list(respostas1.values()),
        color=["blue","red"])
plt.title("Resultado da  Pesquisa Aplicada  pelo McDonalds - 2026")
plt.legend(list(respostas1.keys()),
           loc="upper right",)
#mostrar  o  grafico
plt.show()
'''

#grafico para variaves quantitativas boxplot:
#base  de dados numerica:
dados2 = [15,17,15,15,17,14,18,15,15,17,15,12,15,16]

'''
plt.hist(dados2,bins=3,color="green")
plt.xlabel("Intervalo das quantidades vendidas de camisetas: ")
plt.ylabel("Frequencia absoluta")
plt.title("vendas da Startup FIAP Store")
plt.show()
'''

'''
#  2) Construcao grafica:
plt.boxplot(dados2,
            patch_artist=True,
            boxprops=dict(facecolor='green'))
plt.title("Vendas da Startup One FIAP Store")
plt.xlabel("Dados coletados pela startup em  04/26")
plt.ylabel("quantidade de camisetas vendidas")
plt.show()
'''
#  3) Construcao grafica:
plt.boxplot(dados2,
            patch_artist=True,
            boxprops=dict(facecolor='green'),
            vert=False)
plt.title("Vendas da Startup One FIAP Store")
plt.xlabel("quantidade de camisetas vendidas")
plt.ylabel("Dados coletados pela startup em  04/26")
plt.show()
