import math
import random

print(random.randrange(1,50))
dias = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]

print(random.choice(dias))


numa= float(input("Digite um numero: "))
numb= float(input("Digite um numero: "))
numc= int(input("Digite um numero: "))
numd= int(input("Digite um numero: "))
print(numa)
print(numb)
print(numc)
print(numd)
resultado2 = numc + numd
resultado = numa + numb
print(f"resultado :{math.sqrt(resultado)}")
print(f"resultado int:{math.sqrt(resultado2)}")