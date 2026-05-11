from random import choice
import string

MAX_INCORRECT_GUESSES = 6

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







if __name__ == "__main__":
    pass