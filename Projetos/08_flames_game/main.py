def flames():
    nome1_list = list(input("Digite o primeiro nome: ").lower().replace(" ", ""))
    nome2_list = list(input("Digite o segundo nome: ").lower().replace(" ", ""))

    # Remove letras em comum
    for l in nome1_list[:]:  
        if l in nome2_list:
            print(f"Removeu a letra: {l}")
            nome1_list.remove(l)
            nome2_list.remove(l)

    contador = len(nome1_list) + len(nome2_list)

    print(f"Lista atualizada: {nome1_list + nome2_list}")
    print(f"Contador: {contador}")

    flames_lista = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]

    index = 0

    while len(flames_lista) > 1:
        index = (index + contador - 1) % len(flames_lista)
        removido = flames_lista.pop(index)

        print(f"Removeu: {removido}")
        print(f"Restantes: {flames_lista}")

    print(f"\nResultado final: {flames_lista[0]}")


if __name__ == "__main__":
    flames()