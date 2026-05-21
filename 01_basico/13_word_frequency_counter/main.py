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




if __name__ == "__main__":
    pass

