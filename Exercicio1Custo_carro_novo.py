#Custo de fábrica de um carro novo para o consumidor.

custo_de_fabrica = float(input("Digite o valor de fábrica do carro: R$ "))
porcentagem_distribuidor = 0.12 # 12%
porcentagem_importos = 0.30 # 30%  

# Custos dos valores correspondentes

valor_distribuidor = custo_de_fabrica * porcentagem_distribuidor
valor_impostos = custo_de_fabrica * porcentagem_importos

#Calculo final para o consumidor

custo_consumidor = custo_de_fabrica + valor_distribuidor + valor_impostos

print (f"O custo final para o consumidor é: R$ {custo_consumidor:.2f}")
