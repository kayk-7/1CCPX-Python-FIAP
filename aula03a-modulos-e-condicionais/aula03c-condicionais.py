#OPERADORES DE ATRIBUIÇÃO

num = 15
print(num)

num = num + 2
print(num)

num += 2
print(num)

#OPERADORES RELACIONAIS

print() #pula linha
print(6 >= 6)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)

#OPERADORES LÓGICOS
#LÓGICA E(AND)
print()

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if not login:
    print("po cara acerta ai..")
print()

#NOTAS....

nota_final = 6

if nota_final <4:
    print("reprovado")
elif nota_final <6:
    print("REPROVADO")
else:
    print("APROVADO")

print("fim")
