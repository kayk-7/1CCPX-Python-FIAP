#EXERCICIO 1

pi = 3.14159
raio = 5
ar = pi*(raio**2)
print(f"sua area: {ar}\n")
#EXERCICIO 2

fahre = 15
ce  = (fahre - 32)*5/9
print(f"em celsius: {ce} \n")
#EXERCICIO 4

li = 25
ca = 5
gasto = (li*3)+(ca*2)
print(f"o total gasto foi: {gasto}\n")
#EXERCICIO 5

dis=150
vel=60
per=dis/vel
print(f"a distancia percorrida e: {per}Hrs\n")
#EXERCICIO 6

na = int(input("sua nota 1: "))
nb = int(input("sua nota 2: "))
me = (na + nb)/2

print(f"media final: {me}")
#EXERCICIO 7
nota_a= int(input("Qual nota 1: "))
nota_b= int(input("Qual nota 2: "))
media=((nota_a*4)+(nota_b*56))/10
print(f"A sua média é: {media}")

# proximo
prod= int(input("Valor do produto escolhido: "))
valr= int(input("Dinheiro entregue: "))
tr= valr-prod
print(f"O restante sera: R${tr}, obrigado!")