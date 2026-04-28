SIM = ["sim","s","yes","y"]
NAO = ["não","nao","no","n"]

def realmente_quer_sair():
    while True:
        resposta_user = input("\n❌ Tem certeza que quer sair? (sim/não): ").strip().lower()
        
        if resposta_user in SIM:
            print("\n👋 Obrigado! Até a próxima!")
            return True
        
        elif resposta_user in NAO:
            print("\n🔁 Loading...") 
            return False
        
        else:
            print("\n❌ Resposta não reconhecida. Digite 'sim' ou 'não'.")          
            

def main(): # Entry point 

    print("\nBEM-VINDO AO JOGO DO 21!")
    print("\nEstratégia: múltiplos de 4 são posições de controle (4, 8, 12, 16, 20)")

    while True:
        resposta_user = input("\n🎲 Quer jogar uma partida? (sim/não): ").strip().lower()

        if resposta_user in SIM:
            print("🚧 Jogo ainda não implementado\n") # colocar jogar_partida()
        elif resposta_user in NAO: 
            if realmente_quer_sair():
                break           
        else:
            print("\n❌ Resposta não reconhecida. Digite 'sim' ou 'não'.")


           
if __name__ == "__main__":
    main()