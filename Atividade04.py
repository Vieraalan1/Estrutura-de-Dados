compras = []

def adicionar_item(item):
    compras.append(item)
    print("Item adicionado à lista de compras!")


def remover_item(item):
    if item in compras:
        compras.remove(item)
        print("Item removido da lista de compras!")
    else:
        print("O item não está na lista de compras.")


def listar_itens():
    print("Lista de compras:")
    for item in compras:
        print("- " + item)


while True:
    print("\nO que deseja fazer?")
    print("1 - Adicionar item à lista")
    print("2 - Remover item da lista")
    print("3 - Listar itens da lista")
    print("4 - Sair do programa")

    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == "1":
        item = input("Digite o item que deseja adicionar: ")
        adicionar_item(item)
    elif escolha == "2":
        item = input("Digite o item que deseja remover: ")
        remover_item(item)
    elif escolha == "3":
        listar_itens()
    elif escolha == "4":
        break
    else:
        print("Escolha inválida. Tente novamente.")
