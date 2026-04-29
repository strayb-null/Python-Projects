import sys
import time

SIM = ["sim", "s", "yes", "y"]
NAO = ["não", "nao", "no", "n"]

def jogador_perdeu():
    """Exibe mensagem de derrota e encerra o programa."""
    print("\n" + "=" * 50)
    print("❌ VOCÊ PERDEU! Você foi forçado a dizer 21.")
    print("💡 Dica: tente sempre deixar o adversário em múltiplos de 4.")
    print("=" * 50 + "\n")
    sys.exit(0)


def coleta_numeros_jogador(ultimo_numero, sequencia):
    """Valida a entrada do jogador e atualiza a sequência."""
    max_permitido = min(3, 21 - ultimo_numero)
    
    while True:
        try:
            entrada = input(f"Quantos números você quer dizer? (1 a {max_permitido}): ").strip()
            qtd = int(entrada)
            
            if qtd < 1 or qtd > max_permitido:
                print(f"❌ Valor inválido. Você só pode dizer entre 1 e {max_permitido} número(s).")
                continue
            break
        except ValueError:
            print("❌ Digite um número inteiro válido.")

    # Gera os números consecutivos e atualiza a sequência
    novos_numeros = list(range(ultimo_numero + 1, ultimo_numero + qtd + 1))
    sequencia.extend(novos_numeros)
    print(f"🗣️ Você disse: {novos_numeros}")
    return novos_numeros[-1]


def turno_computador(ultimo_numero, sequencia):
    """IA do computador usando a estratégia dos múltiplos de 4."""
    print("🤖 Vez do computador...")
    time.sleep(1)  # Pequena pausa para parecer mais natural

    # Estratégia vencedora: sempre tentar terminar a rodada em um múltiplo de 4
    proximo_multiplo_4 = ((ultimo_numero // 4) + 1) * 4
    qtd = proximo_multiplo_4 - ultimo_numero

    # Se já estiver em múltiplo de 4 (posição perdedora), joga 1 para induzir erro
    if qtd not in (1, 2, 3):
        qtd = 1

    # Segurança para não ultrapassar 21
    if ultimo_numero + qtd > 21:
        qtd = 21 - ultimo_numero

    novos_numeros = list(range(ultimo_numero + 1, ultimo_numero + qtd + 1))
    sequencia.extend(novos_numeros)
    print(f"🤖 Computador disse: {novos_numeros}")
    return novos_numeros[-1]


def jogar_partida():
    sequencia_completa = []  # Todos os números ditos na partida
    ultimo_numero = 0        # Último número dito (0 = início)
    
    # ----- escolha de quem começa -----
    print("\n" + "-" * 50)
    print("Quem começa?\n")
    print("[1] Você")
    print("[2] Computador (Recomendado!)")
    print("-" * 50)
    
    while True:
        escolha_quem_comeca = input("> ").strip()
        if escolha_quem_comeca in ["1", "2"]:
            break
        print("\n❌ Resposta não reconhecida. Digite '1' ou '2'.")

    print("-" * 50)
    vez_jogador = (escolha_quem_comeca == "1")
    
    if vez_jogador:
        print("\n👤 Você começa!\n")
    else:
        print("\n🤖 Computador começa!\n")

    # =========================================================================
    # LOOP PRINCIPAL DA PARTIDA
    # =========================================================================
    while ultimo_numero < 21:
        print(f"\n📊 Sequência até agora: {sequencia_completa or '[]'}")
        print(f"🔢 Último número dito: {ultimo_numero}")

        if vez_jogador:
            ultimo_numero = coleta_numeros_jogador(ultimo_numero, sequencia_completa)
            if ultimo_numero == 21:
                jogador_perdeu()  # Encerra o programa
        else:
            ultimo_numero = turno_computador(ultimo_numero, sequencia_completa)
            if ultimo_numero == 21:
                print("\n" + "=" * 50)
                print("🎉 VOCÊ VENCEU! O computador foi forçado a dizer 21.")
                print("=" * 50 + "\n")
                return  # Retorna ao menu principal

        # Alterna a vez
        vez_jogador = not vez_jogador


def realmente_quer_sair():
    """Faz um double check antes de encerrar."""
    while True:
        resposta_user = input("\n❌ Tem certeza que quer sair? (sim/não): ").strip().lower()
        
        if resposta_user in SIM:
            print("\n👋 Obrigado! Até a próxima!")
            return True
        elif resposta_user in NAO:
            print("\n🔁 Retornando ao menu...") 
            return False
        else:
            print("\n❌ Resposta não reconhecida. Digite 'sim' ou 'não'.")          


def main():
    print("\n🎮 BEM-VINDO AO JOGO DO 21!")
    print("📜 Regras: Diga 1, 2 ou 3 números consecutivos por vez.")
    print("🎯 Objetivo: NÃO ser quem diz o número 21.")
    print("💡 Estratégia: Múltiplos de 4 (4, 8, 12, 16, 20) são posições de controle.")
    print("-" * 50)
    
    while True:
        resposta_user = input("\n🎲 Quer jogar uma partida? (sim/não): ").strip().lower()
        
        if resposta_user in SIM:
            jogar_partida()
            # Removi o 'break' daqui para permitir jogar várias vezes seguidas.
            # Se quiser encerrar após 1 partida, basta descomentar a linha abaixo:
            # break 
        elif resposta_user in NAO: 
            if realmente_quer_sair():
                break           
        else:
            print("\n❌ Resposta não reconhecida. Digite 'sim' ou 'não'.")

           
if __name__ == "__main__":
    main()