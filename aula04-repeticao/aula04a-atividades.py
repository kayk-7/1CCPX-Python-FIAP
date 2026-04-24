#atividade 02

def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("Nota incorreta(0 a 10)")
        nota = float(input("Digite a primeira nota novamente: "))
    return nota

notaA= float(input("Digite a 1a nota: "))
notaA = validar_nota(notaA)
notaB= float(input("Digite a 1a nota: "))
notaB= validar_nota(notaB)

media = (notaB+notaA)/2


#atividade 01
n = int(input("digite um numero inteiro n:"))

cont = 1
while cont <= n:
    print(cont)
    cont+=1