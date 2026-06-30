#Ler dois número inteitos e fazer a troca dos valores

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

a,b = b,a

#Imprima os valores trocados
print(f"O novo valor de A é: {a}")
print(f"O novo valor de B é: {b}")