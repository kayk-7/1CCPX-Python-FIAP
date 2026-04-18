import pygame
#exercicio 4


#exercicio 3
numea = int(input("Digite um numero: "))
numeb = int(input("Digite outro numero: "))
if numea > numeb:
    print(f"O numero {numea} e maior, e o menor {numeb}.")
elif numeb > numea:
    print(f"O numero {numeb} e maior, e o menor e {numea}.")
else:
    print("Numeros iguais")


#exercicio 2
numero = int(input("Digite um número: "))

if numero & 1:
    print(f"{numero} é ÍMPAR")
else:
    print(f"{numero} é PAR")

#exercicio 1
permissao = input("Tocar musica?[SIM/NAO]")
if permissao in "SIM""s""sim""si":
    # inicia
    pygame.init()
#chama a musica
    pygame.mixer.music.load("audiopapkin-riser-hit-sfx-001-289802.mp3")
#toca a musica
    pygame.mixer.music.play()
    pygame.event.wait()
#necessario para tocar a musica
    input()
else:
    print("FIM!")

def musica_tocar(musica):
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    pygame.event.wait()
    input()
print(musica_tocar("audiopapkin-riser-hit-sfx-001-289802.mp3"))






