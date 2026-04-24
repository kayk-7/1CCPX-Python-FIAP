for cont_music in range(3):
    print(cont_music)

#contar de 1 ate 11, pulando de 2 em 2
for i in range (1,12,2):
    print(i)

#ATIVIDADE
qtd_music= int(input("Digite a quantidade de musicas: "))

for i in range(qtd_music):
    print(f"musica n: {i}")

#LACOS ANINHADOS
#REP. ENCADEADAS

for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f"i:{i} j:{j}")