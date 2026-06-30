import os

# Nome do arquivo onde as tarefas serão salvas
ARQUIVO_DADOS = "tarefas.txt"
tarefas = []

# --- 1. CARREGAR TAREFAS SALVAS ---
# Verifica se o arquivo existe antes de tentar ler
if os.path.exists(ARQUIVO_DADOS):
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        # Lê cada linha do arquivo e remove a quebra de linha (\n)
        tarefas = [linha.strip() for linha in arquivo.readlines()]
    print(f"Sucesso: {len(tarefas)} tarefas carregadas do arquivo!")
else:
    print("Nenhum arquivo de salvamento encontrado. Iniciando lista vazia.")

# --- 2. MENU INTERATIVO ---
while True:
    print("\n--- GERENCIADOR COM SALVAMENTO ---")
    print("1. Adicionar tarefa no final")
    print("2. Inserir tarefa em posição específica")
    print("3. Remover uma tarefa com segurança")
    print("4. Mostrar tarefas (Ordem Alfabética)")
    print("5. Remover última tarefa cadastrada")
    print("6. Salvar e Sair")
    
    print(f"Total de tarefas atual: {len(tarefas)}")
    opcao = input("\nEscolha uma opção (1-6): ").strip()

    if opcao == "1":
        nova_tarefa = input("Digite a tarefa para adicionar: ").strip()
        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print(f"'{nova_tarefa}' adicionada temporariamente à memória!")
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
        if tarefa_remover in tarefas:
            tarefas.remove(tarefa_remover)
            print(f"'{tarefa_remover}' foi removida!")
        else:
            print(f"Aviso: A tarefa '{tarefa_remover}' não existe na lista.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("A lista está vazia.")
        else:
            tarefas_ordenadas = sorted(tarefas)
            print("\nSuas tarefas em ordem alfabética:")
            for i in range(len(tarefas_ordenadas)):
                print(f"{i + 1}. {tarefas_ordenadas[i]}")

    elif opcao == "5":
        if len(tarefas) > 0:
            removida = tarefas.pop()
            print(f"A última tarefa ('{removida}') foi removida!")
        else:
            print("Não há tarefas para remover.")

    elif opcao == "6":
        # --- 3. SALVAR TAREFAS NO ARQUIVO ---
        # Abre o arquivo no modo escrita ("w"). Isso substitui o arquivo antigo pelo atualizado.
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            for tarefa in tarefas:
                arquivo.write(tarefa + "\n") # Escreve a tarefa e pula uma linha
        print("Dados gravados com sucesso no arquivo 'tarefas.txt'.")
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida! Escolha um número de 1 a 6.")