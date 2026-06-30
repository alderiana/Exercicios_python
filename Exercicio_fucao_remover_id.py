lista_de_tarefas = []

def adicionar_tarefa(descricao, prioridade):
    """Adiciona uma nova tarefa à lista como um dicionário."""
    tarefa = {
        "descrição": descricao,
        "prioridade": prioridade,
        "status": "pendente"
    }
    lista_de_tarefas.append(tarefa)
    print(f"\nTarefa '{descricao}' adicionada com sucesso!")

def obter_tarefas_ordenadas():
    """Retorna a lista de tarefas ordenada por prioridade."""
    return sorted(lista_de_tarefas, key=lambda x: x["prioridade"])

def mostrar_tarefas():
    """Mostra todas as tarefas ordenadas por prioridade com um ID numérico."""
    if not lista_de_tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    tarefas_ordenadas = obter_tarefas_ordenadas()

    print("\n=== LISTA DE TAREFAS (Ordenada por Prioridade) ===")
    for i, tarefa in enumerate(tarefas_ordenadas, start=1):
        print(f"ID {i} | [{tarefa['status'].upper()}] - {tarefa['descrição']} (Prioridade: {tarefa['prioridade']})")

def marcar_concluida(id_tarefa):
    """Busca uma tarefa pelo ID correspondente na exibição e a conclui."""
    tarefas_ordenadas = obter_tarefas_ordenadas()
    
    # Verifica se o ID é válido dentro do tamanho atual da lista
    if 1 <= id_tarefa <= len(tarefas_ordenadas):
        # Encontra a tarefa na lista ordenada
        tarefa_alvo = tarefas_ordenadas[id_tarefa - 1]
        # Atualiza a tarefa original dentro da lista_de_tarefas global
        tarefa_alvo["status"] = "concluída"
        print(f"\nTarefa '{tarefa_alvo['descrição']}' marcada como concluída!")
    else:
        print("\nID inválido. Nenhuma tarefa encontrada.")

def remover_tarefa(id_tarefa):
    """Busca uma tarefa pelo ID correspondente na exibição e a remove."""
    tarefas_ordenadas = obter_tarefas_ordenadas()
    
    if 1 <= id_tarefa <= len(tarefas_ordenadas):
        tarefa_alvo = tarefas_ordenadas[id_tarefa - 1]
        lista_de_tarefas.remove(tarefa_alvo)
        print(f"\nTarefa '{tarefa_alvo['descrição']}' removida com sucesso!")
    else:
        print("\nID inválido. Nenhuma tarefa encontrada.")

def pedir_id_valido(mensagem):
    """Garante que o usuário digite um número inteiro para o ID."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite o número do ID (ex: 1, 2, 3).")

def main():
    """Função principal que gerencia o menu interativo."""
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair do programa")
        
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ").strip()
            
            while True:
                try:
                    prioridade = int(input("Digite a prioridade (1 a 5, onde 1 é a mais alta): "))
                    if 1 <= prioridade <= 5:
                        break
                    print("Por favor, digite um número estritamente entre 1 e 5.")
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            
            adicionar_tarefa(descricao, prioridade)

        elif opcao == "2":
            mostrar_tarefas()

        elif opcao == "3":
            if not lista_de_tarefas:
                print("\nNão há tarefas para concluir.")
            else:
                mostrar_tarefas() # Mostra a lista antes para o usuário ver os IDs atualizados
                id_tarefa = pedir_id_valido("\nDigite o ID da tarefa que deseja concluir: ")
                marcar_concluida(id_tarefa)

        elif opcao == "4":
            if not lista_de_tarefas:
                print("\nNão há tarefas para remover.")
            else:
                mostrar_tarefas() # Mostra a lista antes para o usuário ver os IDs atualizados
                id_tarefa = pedir_id_valido("\nDigite o ID da tarefa que deseja remover: ")
                remover_tarefa(id_tarefa)

        elif opcao == "5":
            print("\nSaindo do programa... Até mais!")
            break
            
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()