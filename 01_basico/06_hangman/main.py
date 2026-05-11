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





if __name__ == "__main__":
    pass