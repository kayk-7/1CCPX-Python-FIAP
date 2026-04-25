import pygame


# atividade 4

def horas_extras(salario_base, horas):
    horas_extras =  salario_base*0.015*horas
    return horas_extras
def calcular_desconto_faltas(salario_base, faltas):
    calcular_desconto_faltas = faltas*0.02*salario_base
    return calcular_desconto_faltas
def calcular_bonus(cargo,recebeu_bonus):
    if recebeu_bonus=="s":
        match cargo:
            case 1:
                calcular_bonus=1000
            case 2:
                calcular_bonus=500
            case 3:
                calcular_bonus=300
            case 4:
                calcular_bonus=100
    else:
        calcular_bonus=0
    return calcular_bonus

nome = input("Digite seu nome: ")
cargo  = int(input("Digite seu cargo (1 a 4): "))
while cargo >4:
    print("Apenas valores de 1 a 4")
    cargo = int(input("Digite seu cargo (1 a 4): "))

sal = float(input("Digite seu salario: "))
horaex = int(input("Horas extras trabalhadas: "))
faltas = int(input("Quantas faltas: "))
bonus = input("Recebeu bonus(s ou n): ")

acumu=calcular_bonus(cargo,bonus) + horas_extras(sal,horaex)
desc=calcular_desconto_faltas(sal,faltas)
salfinal=sal+acumu-desc

print(f"Ola {nome}, seu salario bruto foi: {sal},  e teve um  acrescimo de:  {acumu} e um desconto de: {desc}. Seu salario final foi de: {salfinal}")

# atividade 3
cp1 = float(input("Digite a nota do primeiro Checkpoint(0 a 10): "))
cp2 = float(input("Digite a nota do segundo Checkpoint(0 a 10): "))
cp3 = float(input("Digite a nota do terceiro Checkpoint(0 a 10): "))
sp1 = float(input("Digite a nota da primeira Sprint(0 a 10): "))
sp2 = float(input("Digite a nota da segunda Sprint(0 a 10): "))
gs = float(input("Digite a nota do Global Solution(0 a 10): "))

if cp1>10 or cp2>10 or cp3>10 or sp1>10 or sp2>10 or gs>10:
    print("E ATE 10 BURRO")
    exit()
if cp1 < cp2:
    if cp1 < cp3:
            somacps = cp2 + cp3
elif cp2 < cp1:
    if cp2 < cp3:
            somacps = cp1 + cp3
elif cp3 < cp2:
    if cp3 < cp1:
            somacps = cp2 + cp1
elif cp1 == cp2 and cp2 == cp3 and cp1 == cp3:
    somacps = cp1 + cp2

media = ((somacps + sp1 + sp2)/4)*0.4+(gs*0.6)
mediapeso = media*0.4

print(f"Sua media nesse semestre e: {media:.1f}. Agora sua media com peso e: {mediapeso:.1f}.")


# atividade 2
numa = int(input("Digite um numero para descobrir seu triangulo: "))
numb = int(input("Digite outro numero para descobrir seu triangulo: "))
numc = int(input("Digite mais um numero para descobrir seu triangulo: "))
maiornum, medionum, menornum = sorted([numa, numb, numc], reverse=True)
maiornumelev = maiornum**2
medionumelev = medionum**2
menornumelev = menornum**2

if maiornum >= medionum + menornum:
    print("Nao forma triangulo.")
else:
    if maiornumelev == medionumelev + menornumelev:
        print("Triangulo Retangulo.")
    elif maiornumelev > medionumelev + menornumelev:
        print("Triangulo Obtusangulo.")
    elif maiornumelev < medionumelev + menornumelev:
        print("Triangulo Acutangulo.")
    else:
        if maiornum == medionum == menornum:
            print("Triangulo Equilatero.")
        if maiornum == medionum or maiornum == menornum or medionum == menornum:
            print("Triangulo Isosceles.")

# atividade 1

origem = int(input("Origem da carga do caminhao(1 a 5): "))
pesoton = int(input("Peso da carga em toneladas do caminhao: "))
codcarga = int(input("Codigo da carga do caminhao(10 a 40): "))
pesokg = pesoton*1000

if codcarga <=20:
    precocarga = pesokg*100
elif codcarga <=30:
    precocarga = pesokg*250
elif codcarga <=40:
    precocarga = pesokg*340

if origem == 1:
    imposto = 0.35
elif origem == 2:
    imposto = 0.25
elif origem == 3:
    imposto = 0.15
elif origem == 4:
    imposto = 0.05
elif origem == 5:
    imposto = 0

impostocarga = precocarga*imposto
total = impostocarga + precocarga
print(f"O total do seu frete e: {total:.0f}")


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






