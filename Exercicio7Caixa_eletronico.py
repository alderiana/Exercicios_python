def menu():
    print("\n" + "="*30)
    print("       CAIXA ELETRÔNICO       ")
    print("="*30)
    print("1. Consultar saldo")
    print("2. Depositar dinheiro")
    print("3. Sacar dinheiro")
    print("4. Sair")
    print("="*30)

def caixa_eletronico():
    saldo = 0.0  # Saldo inicial fictício

    while True:
        menu()
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

        elif opcao == '2':
            try:
                valor = float(input("\nDigite o valor a depositar: R$ "))
                if valor > 0:
                    saldo += valor
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Valor inválido. O depósito deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

        elif opcao == '3':
            try:
                valor = float(input("\nDigite o valor a sacar: R$ "))
                if 0 < valor <= saldo:
                    saldo -= valor
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                elif valor > saldo:
                    print("Saldo insuficiente para esta operação.")
                else:
                    print("Valor inválido. O saque deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

        elif opcao == '4':
            print("\nObrigado por utilizar nossos serviços. Volte sempre!")
            break

        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")

# Executa o programa
caixa_eletronico()