# atividade 5
def pode_aprovar(idade,rendamensal,emprestimo):
    if idade > 18:
        if emprestimo <rendamensal*20:
            print("Emprestimo aprovado")
        elif  emprestimo >  rendamensal*20:
            print("Emprestimo recusado")
            exit()
    else:
        print("Emprestimo recusado")
        exit()
def definir_taxa(parcelas):
    if parcelas<=6:
        taxa=0.05
    elif parcelas >6 and parcelas<=12:
        taxa=0.08
    elif parcelas >12 and parcelas<=24:
        taxa=0.10
    return taxa
def calcular_parcelas(valor,tax,parcelas):
    resultado = (valor * tax * (1+tax) ** parcelas) / ((1+tax)**parcelas-1)
    return resultado
def calcular_total(parcela,parcelas):
    calcular_total = parcela*parcelas
    return calcular_total
def calcular_juros(total,valor):
    calcular_juros = total-valor
    return calcular_juros
nome=input('Escreva seu nome: ')
idade=int(input('Escreva sua idade: '))
renda_mensal=int(input('Escreva a sua renda mensal: '))
emprestimo=int(input('Escreva o valor do emprestimo: '))
nparcelas=int(input('Escreva a quantidade de parcelas: '))
print(pode_aprovar(idade,renda_mensal,emprestimo))
taxas = definir_taxa(nparcelas)
valor_parcela = calcular_parcelas(emprestimo,taxas,nparcelas)
valor_total_pago = calcular_total(valor_parcela,nparcelas)
juros_pagos = calcular_juros(valor_total_pago,emprestimo)
print(f"Ola {nome}, o seu emprestimo de: {emprestimo}, vai ter {taxas}% ao mes, resultando em {valor_parcela:.2f} por mes, sendo pago ao total  {valor_total_pago:.2f} e desse valor {juros_pagos:.2f} e so de juros.")