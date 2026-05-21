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
    
def clean_and_tokenize(text: str):
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



if __name__ == "__main__":
    pass

