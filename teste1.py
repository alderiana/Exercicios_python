tarefas = []
tarefas.append("estudar")
tarefas.append("correr")
tarefas.append("nadar")
print("tarefas iniciais:")
print(tarefas)

tarefas.insert(0, "tomar café")

tarefas.remove("nadar")

print("\ntarefas após alterações:")
for i in range(len(tarefas)):
    print(f"{i + 1}.{tarefas[i]}")

tarefas.sort()
print("\ntarefas em ordem alfabétiva:")
print(tarefas)

tarefas.reverse()
print(f"\ntarefas em ordem reserva:")
print(tarefas)

ultima = tarefas.pop()
print(f"\núltima tarefa removida: {ultima}")

print(f"\nnúmero de tarefas restantes: {len(tarefas)}")

"""para aqui"""






#Exercico como menu interativo opcao2

# Inicializa a lista de tarefas vazia
tarefas = []

while True:
    # Mostra o menu de opções
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar tarefa no final")
    print("2. Inserir tarefa em posição específica")
    print("3. Remover uma tarefa com segurança")
    print("4. Mostrar tarefas (Ordem Alfabética)")
    print("5. Remover última tarefa cadastrada")
    print("6. Sair")
    
    # Mostra o total de tarefas atual
    print(f"Total de tarefas atual: {len(tarefas)}")
    
    opcao = input("\nEscolha uma opção (1-6): ").strip()

    if opcao == "1":
        nova_tarefa = input("Digite a tarefa para adicionar: ").strip()
        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print(f"'{nova_tarefa}' adicionada ao final!")
        else:
            print("Operação cancelada: texto vazio.")

    elif opcao == "2":
        nova_tarefa = input("Digite a tarefa para inserir: ").strip()
        if nova_tarefa:
            try:
                posicao = int(input(f"Digite a posição (0 até {len(tarefas)}): "))
                tarefas.insert(posicao, nova_tarefa)
                print(f"'{nova_tarefa}' inserida na posição {posicao}!")
            except ValueError:
                print("Erro: Você precisa digitar um número válido para a posição.")
        else:
            print("Operação cancelada: texto vazio.")

    elif opcao == "3":
        tarefa_remover = input("Digite o nome exato da tarefa para remover: ").strip()
        # Proteção usando a Opção 1 que vimos antes
        if tarefa_remover in tarefas:
            tarefas.remove(tarefa_remover)
            print(f"'{tarefa_remover}' foi removida com sucesso!")
        else:
            print(f"Aviso: A tarefa '{tarefa_remover}' não existe na lista.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("A lista está vazia.")
        else:
            # Cria uma cópia ordenada para não estragar a ordem original inserida pelo usuário
            tarefas_ordenadas = sorted(tarefas)
            print("\nSuas tarefas em ordem alfabética:")
            for i in range(len(tarefas_ordenadas)):
                print(f"{i + 1}. {tarefas_ordenadas[i]}")

    elif opcao == "5":
        if len(tarefas) > 0:
            # Remove o último elemento usando pop()
            removida = tarefas.pop()
            print(f"A última tarefa ('{removida}') foi removida!")
        else:
            print("Não há tarefas para remover.")

    elif opcao == "6":
        print("Saindo do programa. Até mais!")
        break  # Quebra o laço while e encerra o código

    else:
        print("Opção inválida! Escolha um número de 1 a 6.")