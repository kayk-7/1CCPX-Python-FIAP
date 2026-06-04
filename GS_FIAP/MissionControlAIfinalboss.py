import random

# ============================================================
# DADOS DA MISSÃO
# ============================================================

nome_missao = "Orion Test Alpha"
nome_equipe = "Equipe Apollo"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(temp):

    if temp < 18:
        return "ATENCAO", 1
    elif temp <= 30:
        return "NORMAL", 0
    elif temp <= 35:
        return "ATENCAO", 1
    else:
        return "CRITICO", 2


def analisar_comunicacao(com):

    if com < 30:
        return "CRITICO", 2
    elif com < 60:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(bat):

    if bat < 20:
        return "CRITICO", 2
    elif bat < 50:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(oxi):

    if oxi < 80:
        return "CRITICO", 2
    elif oxi < 90:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(est):

    if est < 40:
        return "CRITICO", 2
    elif est < 70:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0


# ============================================================
# CLASSIFICAÇÃO DO CICLO
# ============================================================

def classificar_ciclo(risco):

    if risco <= 2:
        return "MISSAO ESTAVEL"

    elif risco <= 5:
        return "MISSAO EM ATENCAO"

    else:
        return "MISSAO CRITICA"


# ============================================================
# TENDÊNCIA DA MISSÃO
# ============================================================

def analisar_tendencia(lista_riscos):

    primeiro = lista_riscos[0]
    ultimo = lista_riscos[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."

    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável em relação ao início."


# ============================================================
# RECOMENDAÇÕES
# ============================================================

def gerar_recomendacao(temp_status,com_status,bat_status,oxi_status,est_status):

    recomendacoes = []

    if temp_status == "CRITICO":
        recomendacoes.append(
            "Verificar controle térmico."
        )

    if com_status == "CRITICO":
        recomendacoes.append(
            "Restabelecer comunicação."
        )

    if bat_status == "CRITICO":
        recomendacoes.append(
            "Ativar economia de energia."
        )

    if oxi_status == "CRITICO":
        recomendacoes.append(
            "Acionar suporte à vida."
        )

    if est_status == "CRITICO":
        recomendacoes.append(
            "Reduzir operações não essenciais."
        )

    if len(recomendacoes) == 0:
        return "Manter operação normal."

    return " | ".join(recomendacoes)


# ============================================================
# GERAÇÃO DOS DADOS
# ============================================================

dados_missao = [
 [24, 92, 88, 96, 90],
 [27, 80, 72, 94, 85],
 [31, 65, 58, 91, 70],
 [36, 42, 38, 87, 55],
 [39, 28, 19, 78, 35],
 [34, 55, 32, 82, 50]
]

# ============================================================
# VARIÁVEIS DE CONTROLE
# ============================================================

lista_riscos = []

areas_risco = [0, 0, 0, 0, 0]

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

# ============================================================
# CABEÇALHO
# ============================================================

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)

print("Missão:", nome_missao)
print("Equipe:", nome_equipe)
print("Quantidade de ciclos:", len(dados_missao))

print("=" * 60)

# ============================================================
# ANÁLISE DOS CICLOS
# ============================================================

numero_ciclo = 0

for ciclo in dados_missao:

    numero_ciclo += 1

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    soma_temp += temperatura
    soma_com += comunicacao
    soma_bat += bateria
    soma_oxi += oxigenio
    soma_est += estabilidade

    temp_status, temp_pontos = analisar_temperatura(
        temperatura)

    com_status, com_pontos = analisar_comunicacao(
        comunicacao)

    bat_status, bat_pontos = analisar_bateria(
        bateria)

    oxi_status, oxi_pontos = analisar_oxigenio(
        oxigenio)

    est_status, est_pontos = analisar_estabilidade(
        estabilidade)

    risco_total = (
            temp_pontos +
            com_pontos +
            bat_pontos +
            oxi_pontos +
            est_pontos
    )

    lista_riscos.append(risco_total)

    areas_risco[0] += temp_pontos
    areas_risco[1] += com_pontos
    areas_risco[2] += bat_pontos
    areas_risco[3] += oxi_pontos
    areas_risco[4] += est_pontos

    classificacao = classificar_ciclo(
        risco_total)

    recomendacao = gerar_recomendacao(
        temp_status,
        com_status,
        bat_status,
        oxi_status,
        est_status
    )

    print(f"\nCICLO {numero_ciclo}")
    print("-" * 60)

    print(
        f"Temperatura: {temperatura}°C | {temp_status}"
    )

    print(
        f"Comunicação: {comunicacao}% | {com_status}"
    )

    print(
        f"Bateria: {bateria}% | {bat_status}"
    )

    print(
        f"Oxigênio: {oxigenio}% | {oxi_status}"
    )

    print(
        f"Estabilidade: {estabilidade}% | {est_status}"
    )

    print(
        f"Pontuação de risco: {risco_total}"
    )

    print(
        f"Classificação: {classificacao}"
    )

    print(
        f"Recomendação: {recomendacao}"
    )

# ============================================================
# RELATÓRIO FINAL
# ============================================================

print("\n")
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

media_temp = soma_temp / len(dados_missao)
media_com = soma_com / len(dados_missao)
media_bat = soma_bat / len(dados_missao)
media_oxi = soma_oxi / len(dados_missao)
media_est = soma_est / len(dados_missao)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print(f"Média temperatura: {media_temp:.2f}")
print(f"Média comunicação: {media_com:.2f}")
print(f"Média bateria: {media_bat:.2f}")
print(f"Média oxigênio: {media_oxi:.2f}")
print(f"Média estabilidade: {media_est:.2f}")

# ciclo mais crítico

maior_risco = lista_riscos[0]
ciclo_critico = 1

for i in range(len(lista_riscos)):

    if lista_riscos[i] > maior_risco:
        maior_risco = lista_riscos[i]
        ciclo_critico = i + 1

print(f"Ciclo mais crítico: {ciclo_critico}")
print(f"Maior risco: {maior_risco}")

# risco médio

soma_riscos = 0

for risco in lista_riscos:
    soma_riscos += risco

risco_medio = soma_riscos / len(lista_riscos)

print(f"Risco médio: {risco_medio:.2f}")

# ciclos críticos

qtd_criticos = 0

for risco in lista_riscos:
    if risco >= 6:
        qtd_criticos += 1

print(f"Ciclos críticos: {qtd_criticos}")

print(analisar_tendencia(lista_riscos))

# pontuação por área

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):

    print(
        f"{areas_monitoradas[i]}: "
        f"{areas_risco[i]} pontos"
    )

# área mais afetada

indice_maior = 0

for i in range(len(areas_risco)):

    if areas_risco[i] > areas_risco[indice_maior]:
        indice_maior = i

print("\nÁrea mais afetada:")
print(areas_monitoradas[indice_maior])

# classificação final

if risco_medio <= 2:
    classificacao_final = "MISSAO ESTAVEL"

elif risco_medio <= 5:
    classificacao_final = "MISSAO EM ATENCAO"

else:
    classificacao_final = "MISSAO CRITICA"

print("\nClassificação final:")
print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "MISSAO ESTAVEL":
    print("A missão operou dentro dos padrões esperados.")

elif classificacao_final == "MISSAO EM ATENCAO":
    print("A missão apresentou instabilidades moderadas.")

else:
    print("A missão apresentou falhas críticas e requer intervenção imediata.")