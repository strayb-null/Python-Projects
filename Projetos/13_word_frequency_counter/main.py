import string
import os

def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{filepath}' não encontrado.")
        return None
    except Exception as e:
        print(f"[ERRO] Falha ao ler o arquivo: {e}")
        return None
    
def clean_and_tokenize(text):
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, ' ')
    
    words = text.split()

    stop_words = {
        'a', 'o', 'e', 'de', 'do',
        'da', 'em', 'um', 'uma',
        'que', 'para', 'com', 'os',
        'as', 'no', 'na', 'se',
    }

    clean_words = []
    for word in words:
        if word not in stop_words:
            clean_words.append(word)

    return clean_words

def count_words(word_list):
    frequency = {}

    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

def show_results(frequency: dict[str, int], top_n=10):
    if not frequency:
        print("Nenhuma palavra encontrada.")
        return
    
    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n" + "="*40)
    print(f"  TOP {top_n} PALAVRAS MAIS FREQUENTES")
    print("="*40)

    for i, (word, count) in enumerate(sorted_words[:top_n], start=1):
        bar = "█" * count
        print(f"  {i:>2}. {word:<15} {count:>4}x  {bar}")

    print("="*40)
    print(f"  Total de palavras únicas: {len(frequency)}")
    print("="*40 + "\n")

def main():
    default_file = "texto.txt"

    if not os.path.exists(default_file):
        print(f"[INFO] Criando arquivo de exemplo...")

        with open(default_file, "w", encoding="utf-8") as f:
            f.write("Python é uma linguagem de programação poderosa e versátil.\n")
            f.write("Programação em Python é acessível para iniciantes.\n")
            f.write("Muitos engenheiros de software usam Python no dia a dia.\n")
            f.write("Python domina a área de ciência de dados e machine learning.\n")
            f.write("Aprender Python vale muito a pena para qualquer programador.\n")
        print(f"[INFO] Arquivo '{default_file}' criado!\n")

    while True: 
        print("Analisador de Frequência de Palavras")
        print("--------------------------------------")
        filepath = input(f"Digite o nome do arquivo [{default_file}]: ").strip()

        if filepath == "":
            filepath = default_file

        if filepath.lower() == 'sair':
            print("Encerrando. Até mais!")
            break

        content = read_file(filepath)

        if content is None:
            print("Tente novamente.\n")
            continue

        words = clean_and_tokenize(content)
        frequency = count_words(words)
        show_results(frequency)
        again = input("Analisar outro arquivo? (s/n): ").strip().lower()

        if again != 's':
            print("Encerrando. Até mais!")
            break




if __name__ == "__main__":
    main()

