# Lista global para armazenar as tarefas
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

def mostrar_tarefas():
    """Mostra todas as tarefas ordenadas por prioridade (1 é a maior)."""
    if not lista_de_tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    # Ordena a lista: prioridade 1 (maior) aparece primeiro
    tarefas_ordenadas = sorted(lista_de_tarefas, key=lambda x: x["prioridade"])

    print("\n=== LISTA DE TAREFAS (Ordenada por Prioridade) ===")
    for i, tarefa in enumerate(tarefas_ordenadas, start=1):
        print(f"{i}. [{tarefa['status'].upper()}] - {tarefa['descrição']} (Prioridade: {tarefa['prioridade']})")

def marcar_concluida(descricao_procurada):
    """Busca uma tarefa pela descrição e altera seu status para concluída."""
    encontrada = False
    for tarefa in lista_de_tarefas:
        # Comparação ignorando maiúsculas/minúsculas e espaços extras
        if tarefa["descrição"].strip().lower() == descricao_procurada.strip().lower():
            tarefa["status"] = "concluída"
            print(f"\nTarefa '{tarefa['descrição']}' marcada como concluída!")
            encontrada = True
            break
    
    if not encontrada:
        print(f"\nTarefa '{descricao_procurada}' não encontrada.")

def main():
    """Função principal que gerencia o menu interativo."""
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair do programa")
        
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ").strip()
            
            # Validação simples para garantir que a prioridade seja de 1 a 5
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
                nome_tarefa = input("Digite o nome exato da tarefa que deseja concluir: ")
                marcar_concluida(nome_tarefa)

        elif opcao == "4":
            print("\nSaindo do programa... Até mais!")
            break
            
        else:
            print("\nOpção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()