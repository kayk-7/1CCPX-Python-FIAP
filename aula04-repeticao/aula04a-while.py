#sistema decrescente 4 ate 1

dec = 4
while dec > 0:
    print(dec)
    dec -= 1

# repeticao com entrada do usuario
jogar= "Sim"
while jogar.lower()== "sim":
    print("iniciar jogo")
    input("jogar novamente")


# excessao/filtracao
i=0
while i<10:
    i+=1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"produto: {i}")

