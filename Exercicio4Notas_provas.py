# Leitura das notas de prova e trabalhos
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))
t1 = float(input("Digite a nota do T1: "))
t2 = float(input("Digite a nota do T2: "))

# Cálculos
mp = (p1 + p2) / 2
mt = (t1 + t2) / 2
mf = 0.8 * mp + 0.2 * mt

# Exibição da média final (opcional, mas recomendado)
print(f"Média Final: {mf:.2f}")

# Verificação da situação
if mf >= 6.0:
    print("Aprovado")
else:
    print("Não aprovado")