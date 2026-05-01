# Preparando o ambiente:
from collections import Counter
import pandas as pd

#Configurar a saida da tabela final:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#Criar a base de  dados:
dados = [14]*6+[15]*12+[16]*9+[17]*3

#Curiosidade
# print(type(dados))

#frequencia  absoluta:
fi = pd.Series(Counter(dados)).sort_index()
print(fi)

#frequencia absoluta acumulada:
fia = fi.cumsum()
print(fia)

#frequencia relativa:
fr =  fi / fi.sum()*100
print(fr)

#frequencia relativa acumulada:
fra = fr.cumsum()
print(fra)

# montar a  tabela:
tabela = pd.DataFrame({
    'Frequancia absoluta': fi,
    'Frequancia absoluta acumulada': fia,
    'Frequancia relativa': fr,
    'Frequancia relativa acumulada': fra
})
print(tabela)

total_row=pd.Series({
    'Frequancia absoluta': fi.sum(),
    'Frequancia absoluta acumulada': '-',
    'Frequancia relativa': fr.sum(),
    'Frequancia relativa acumulada': '-'
}, name='total')
print(total_row)

tabela = pd.concat([tabela, total_row.to_frame().T])
print(tabela)