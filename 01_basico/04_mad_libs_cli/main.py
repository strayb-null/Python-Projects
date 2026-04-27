import time

def historia_um_dia_memoravel():
    print("\n--- Um Dia Memorável ---")
    print("Preencha as palavras abaixo para gerar a história:\n")
    
    # Coletando os dados do usuário
    nome = input("Digite um nome: ")
    esporte = input("Digite um esporte: ")
    cidade = input("Digite uma cidade: ")
    jogador = input("Digite o nome de um jogador famoso: ")
    bebida = input("Digite o nome de uma bebida: ")
    lanche = input("Digite o nome de um lanche: ")
    
    # Criando a história usando f-strings
    historia = f"""
    Um dia, eu e meu amigo {nome} decidimos jogar uma partida de {esporte} em {cidade}.
    Nós queríamos assistir o {jogador} jogar.
    Depois do jogo, bebemos {bebida} e também comemos alguns {lanche}.
    Nós realmente nos divertimos! Estamos ansiosos para voltar e jogar novamente.
    """
    
    print("\nGerando história...")
    time.sleep(1) # Pequena pausa para efeito dramático
    print(historia)    

def menu_principal():
    while True:
        print("\n==========================================================")
        print("""   
███╗   ███╗ █████╗ ██████╗     ██╗     ██╗██████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗    ██║     ██║██╔══██╗██╔════╝
██╔████╔██║███████║██║  ██║    ██║     ██║██████╔╝███████╗
██║╚██╔╝██║██╔══██║██║  ██║    ██║     ██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║  ██║██████╔╝    ███████╗██║██████╔╝███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚══════╝ 
""".strip())
        print("==========================================================")
        print("1. Um Dia Memorável")
        print("2. Sair")
        
        escolha = input("\nEscolha uma opção (1 ou 2): ")

        if escolha == '1':
            historia_um_dia_memoravel()
        elif escolha == '2':
            print("Obrigado por jogar! Até logo.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
        
        # Pergunta se quer continuar
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! Até logo.")
            break

if __name__ == "__main__":
    menu_principal()