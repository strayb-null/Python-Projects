from random import choice
import string

TOTAL_PALPITES_ERRADOS = 6

# ═══════════════════════════════════════════════════════════
# ETAPA 1: Selecionar a palavra secreta
# ═══════════════════════════════════════════════════════════

def selecionar_palavra():
    """Lê o arquivo words.txt e retorna uma palavra aleatória."""
    with open("palavras.txt", mode="r") as palavras:
        lista_palavras = palavras.readlines()
        return choice(lista_palavras).strip()

# ═══════════════════════════════════════════════════════════
# ETAPA 2: Validar a entrada do jogador
# ═══════════════════════════════════════════════════════════

def _validar_input(input_jogador, inputs_anteriores_jogador):
    """ Verifica se o input do jogador é válido """
    return (
        len(input_jogador) == 1
        and input_jogador in string.ascii_lowercase
        and input_jogador not in inputs_anteriores_jogador        
    )

def get_input_jogador(inputs_anteriores_jogador):
    """ Pede um letra ao jogador e valida """
    while True:
        input_jogador = input("Digite uma letra\n> ")
        if _validar_input(input_jogador, inputs_anteriores_jogador):
            return input_jogador
        print("Entrada inválida. Digite uma letra de a-z que ainda não usou.\n ")

# ═══════════════════════════════════════════════════════════
# ETAPA 3: Mostrar o estado do jogo
# ═══════════════════════════════════════════════════════════
def mostrar_letras_tentadas(inputs_anteriores_jogador):
    """Mostra as letras já usadas em ordem alfábetica"""
    return " | ".join(sorted(inputs_anteriores_jogador))

def criar_palavra_adivinhada(palavra_alvo, inputs_anteriores_jogador):
    """Constrói a palavra com underscores para letras não adivinhadas."""
    letras_atuais = []
    for letra in palavra_alvo:
        if letra in inputs_anteriores_jogador:
            letras_atuais.append(letra)
        else:
            letras_atuais.append("_")
    return " ".join(letras_atuais)

def desenha_enforcado(palpites_errados):
    """Desenha o estado atual do enforcado."""
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]
    print(hanged_man[palpites_errados])

# ═══════════════════════════════════════════════════════════
# ETAPA 5: Verificar fim de jogo
# ═══════════════════════════════════════════════════════════

def fim_de_jogo(palpites_errados, palavra_alvo, inputs_anteriores_jogador):
    """Retorna True se o jogo acabou (vitória ou derrota)."""
    if palpites_errados == TOTAL_PALPITES_ERRADOS:
        return True # eu perdi
    if set(palavra_alvo) <= inputs_anteriores_jogador:
        return True
    return False

# ═══════════════════════════════════════════════════════════
# ETAPA 6: Loop principal do jogo
# ═══════════════════════════════════════════════════════════
    
def main():
    """Função principal que executa o jogo."""
    
    # ─── Setup inicial ───
    palavra_alvo = selecionar_palavra()
    inputs_anteriores_jogador = set() 
    palpite_palavra = criar_palavra_adivinhada(palavra_alvo, inputs_anteriores_jogador)
    palpites_errados = 0
    
    print("=" * 50)
    print("  🎮 BEM-VINDO AO HANGMAN! 🎮")
    print("=" * 50)
    print(f"A palavra tem {len(palavra_alvo)} letras.\n")

    # ─── Game loop ───
    while not fim_de_jogo(palpites_errados, palavra_alvo, inputs_anteriores_jogador):
        desenha_enforcado(palpites_errados)
        print(f"\nSua palavra:  {palpite_palavra}")
        print(f"Letras usadas: {mostrar_letras_tentadas(inputs_anteriores_jogador)}")
        print(f"Erros: {palpites_errados}/{TOTAL_PALPITES_ERRADOS}\n")

        player_guess = get_input_jogador(inputs_anteriores_jogador)

        if player_guess in palavra_alvo:
            print("✅ Boa! A letra está na palavra!\n")
        else:
            print("❌ Errou! Essa letra não está na palavra.\n")
            palpites_errados += 1

        inputs_anteriores_jogador.add(player_guess)
        palpite_palavra = criar_palavra_adivinhada(palavra_alvo, inputs_anteriores_jogador)

    # ─── Fim de jogo ───
    desenha_enforcado(palpites_errados)
    print("=" * 50)
    
    if palpites_errados == TOTAL_PALPITES_ERRADOS:
        print("  💀 VOCÊ PERDEU!")
    else:
        print("  🎉 PARABÉNS! VOCÊ VENCEU!")
    
    print(f"  A palavra era: {palavra_alvo.upper()}")
    print("=" * 50)




if __name__ == "__main__":
    main()