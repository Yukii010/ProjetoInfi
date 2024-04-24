import os

# Função para limpar a tela do terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para adicionar uma nova tarefa
def adicionar_tarefa(lista_de_tarefas):
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade da tarefa: ")
    categoria = input("Categoria da tarefa: ")
    tarefa = {'nome': nome, 'descrição': descricao, 'prioridade': prioridade, 'categoria': categoria, 'concluída': False}
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas(lista_de_tarefas):
    clear_screen()
    if not lista_de_tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(lista_de_tarefas, start=1):
            concluida = "Sim" if tarefa['concluída'] else "Não"
            print(f"Tarefa {i}: {tarefa['nome']} - Descrição: {tarefa['descrição']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']} - Concluída: {concluida}")

# Função para marcar uma tarefa como concluída
def marcar_como_concluida(lista_de_tarefas):
    listar_tarefas(lista_de_tarefas)
    indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas[indice]['concluída'] = True
        print("Tarefa marcada como concluída com sucesso!")
    else:
        print("Índice inválido.")

# Função para exibir tarefas por prioridade
def exibir_por_prioridade(lista_de_tarefas):
    prioridade_desejada = input("Digite a prioridade desejada (Alta, Média, Baixa): ").capitalize()
    tarefas_filtradas = [tarefa for tarefa in lista_de_tarefas if tarefa['prioridade'] == prioridade_desejada]
    if tarefas_filtradas:
        print(f"Tarefas com prioridade {prioridade_desejada}:")
        for tarefa in tarefas_filtradas:
            print(f"- {tarefa['nome']}")
    else:
        print(f"Nenhuma tarefa com prioridade {prioridade_desejada} encontrada.")

# Função para exibir tarefas por categoria
def exibir_por_categoria(lista_de_tarefas):
    categoria_desejada = input("Digite a categoria desejada: ")
    tarefas_filtradas = [tarefa for tarefa in lista_de_tarefas if tarefa['categoria'] == categoria_desejada]
    if tarefas_filtradas:
        print(f"Tarefas na categoria {categoria_desejada}:")
        for tarefa in tarefas_filtradas:
            print(f"- {tarefa['nome']}")
    else:
        print(f"Nenhuma tarefa na categoria {categoria_desejada} encontrada.")

# Função principal do programa
def main():
    lista_de_tarefas = []

    while True:
        clear_screen()
        print("===== GERENCIADOR DE TAREFAS =====")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa(lista_de_tarefas)
        elif opcao == '2':
            listar_tarefas(lista_de_tarefas)
            input("Pressione Enter para continuar...")
        elif opcao == '3':
            marcar_como_concluida(lista_de_tarefas)
            input("Pressione Enter para continuar...")
        elif opcao == '4':
            exibir_por_prioridade(lista_de_tarefas)
            input("Pressione Enter para continuar...")
        elif opcao == '5':
            exibir_por_categoria(lista_de_tarefas)
            input("Pressione Enter para continuar...")
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
