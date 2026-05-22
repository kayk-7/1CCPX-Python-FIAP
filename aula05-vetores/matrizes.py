# # tabuleiro 4x5
# tabuleiro = [[i for i in range(1, 6)] for a in range(4)]
#
# print(tabuleiro)
#
# # tabela com os numeros  ate 20
# tabuleiro = [list(range(i, i+5)) for i in range(1, 21, 5)]
#
# print(tabuleiro)

#tabuleiro 4x5 de 1 ate 20
tabuleiro= [
    [' ' ,' ', ' ', ' ', ' '],
    [' ' ,' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]
numer=0
for linha in range(len(tabuleiro)):
    for coluna in range(len(tabuleiro[linha])):
        numer += 1
        tabuleiro[linha][coluna] = numer

