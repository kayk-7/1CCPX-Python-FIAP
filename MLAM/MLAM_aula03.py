#Preparo do ambiente
import pandas as pd
from matplotlib import pyplot as plt

#conjunto de dados;
vendas_camisetas = pd.Series([2,4,3,4,5,2,4,11,4,2])
print(vendas_camisetas)

#analise exploratoria de dados;  etapa de estatistica descritiva
#medidas de tendencia central;
#1)media: esperanca matematica
print(vendas_camisetas.mean())

#2)mediana:Elemento central, separa os conjuntos de dados ao meio,50% dos dados ficam abaixo dela e 50% acima
print(vendas_camisetas.median())

#3)moda: Elemento com maior frequencia absoluta
print(vendas_camisetas.mode())

#medidas de dispersao(variabilidade dos dados):
#1) maximo:
print(vendas_camisetas.max())

#2) minimo:
print(vendas_camisetas.min())

#3) amplitude:
print(vendas_camisetas.max() - vendas_camisetas.min())

#4) Variância Amostral:  nao e interpretavel  pois  a grandeza da variavel e alterada
print(vendas_camisetas.var())

#5) Desvio padrao  Amostral:
print(vendas_camisetas.std())

#6) coeficiente da variacao Amostral(variabilidade dos dados em  %):
print(vendas_camisetas.std()/vendas_camisetas.mean()*100)

# Medidas Separatriz
#  Quartis
print(vendas_camisetas.quantile([0.25,0.50,0.75]))

# Analise Grafica: Boxplot
plt.boxplot(vendas_camisetas,
            patch_artist=True,
            boxprops=dict(facecolor='red'))
plt.show()

print(vendas_camisetas.describe())
