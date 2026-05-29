import string

alfabeto = string.ascii_lowercase


def cifrar(texto: str, chave: int) -> str:
    """
    Cifra um texto usando a Cifra de César.

    Args:
        texto: mensagem a ser criptografada.
        chave: número de deslocamento (1-26).

    Returns:
        Texto cifrado como string.

    Example:
        >>> cifrar("bazinga", 20)
        'vutchau'
    """
    resultado = []
    for l in texto.lower().strip():
        if l in alfabeto:
            idx = (alfabeto.index(l) + chave) % 26
            resultado.append(alfabeto[idx])
        else:
            resultado.append(l)
    mensagem = "".join(resultado)
    print("\n✅ Mensagem criptografada:", mensagem)
    return mensagem


def decifrar(texto: str, chave: int) -> str:
    """
    Decifra um texto usando a Cifra de César.

    Args:
        texto: mensagem a ser decriptografada.
        chave: número de deslocamento (1-26).

    Returns:
        Texto decifrado como string.

    Example:
        >>> decifrar("vutchau", 20)
        'bazinga'
    """
    resultado = []
    for l in texto.lower().strip():
        if l in alfabeto:
            idx = (alfabeto.index(l) - chave) % 26
            resultado.append(alfabeto[idx])
        else:
            resultado.append(l)
    mensagem = "".join(resultado)
    print("\n✅ Mensagem decifrada:", mensagem)
    return mensagem


if __name__ == "__main__":
    cifrar("bazinga", 20)
    decifrar("vutchau", 20)