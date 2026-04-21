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


