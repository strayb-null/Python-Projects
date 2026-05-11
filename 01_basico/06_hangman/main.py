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




if __name__ == "__main__":
    selecionar_palavra()


