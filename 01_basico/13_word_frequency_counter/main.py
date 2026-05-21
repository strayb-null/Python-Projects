import string
import os

def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8"):
            content = filepath.read()
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


if __name__ == "__main__":
    pass

