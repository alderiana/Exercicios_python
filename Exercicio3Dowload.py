#Digite um tamanho de arquivo em dowload

tamanho_mb = float(input("Digite o tamanho do arquivo para dowload (em Mb): "))
velocidade_mbps = float(input("Digite a velocidade de um link de internet (em Mbps): "))

# 1 MB = 8 Megabits. Converter o tamanho do arquivo para Megabits
tamanho_megabits = tamanho_mb * 8

# Calcula o tempo total em segundos
tempo_em_segundo = tamanho_mb / velocidade_mbps

# Converte o tempo de segundos para minutos
tempo_em_minutos = tempo_em_segundo / 60

# Exibe o resultado formatado (com 2 casas decimais)
print(f"\nTempo aproximado de dowload: {tempo_em_minutos:.2f} minutos.")

