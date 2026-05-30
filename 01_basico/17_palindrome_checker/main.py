def palindrome_two_pointers(palavra: str) -> None:
    i = 0
    j = len(palavra) - 1
    palindromo = True

    while i < j:
        if palavra[i] != palavra[j]:
            palindromo = False
            break

        i += 1
        j -= 1

    if palindromo:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


def palindrome_using_all(palavra: str) -> None:
    if all(palavra[i] == palavra[-i - 1] for i in range(len(palavra) // 2)):
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


def palindrome_using_slicing(palavra: str) -> None:
    if palavra == palavra[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


def palindrome_using_reversed(palavra: str) -> None:
    rev = ''.join(reversed(palavra))

    if palavra == rev:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


if __name__ == "__main__":
    palavra = "malayalam"

    print(f"Palavra: {palavra}\n")

    print("→ Two Pointers:")
    palindrome_two_pointers(palavra)

    print("\n→ Using all():")
    palindrome_using_all(palavra)

    print("\n→ Using Slicing:")
    palindrome_using_slicing(palavra)

    print("\n→ Using reversed():")
    palindrome_using_reversed(palavra)