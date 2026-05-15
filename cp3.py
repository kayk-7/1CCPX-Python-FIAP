
temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]
sala1 = temperaturas[0]
sala2 = temperaturas[1]
sala3 = temperaturas[2]
sala4 = temperaturas[3]

c = 1

for sala in temperaturas:

    soma = 0
    rc = 0
    for valor in sala:
        soma += valor

        if valor >= 33:
            rc+=1

    media = soma/4

    print(f"Sala {c}")
    print(f"Média: {media}")
    print(f"Registros Críticos: {rc}")
    print()
    c+=1