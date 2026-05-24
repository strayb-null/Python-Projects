# 📊 Contador de Frequência de Palavras

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![CLI](https://img.shields.io/badge/Interface-Terminal-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=flat-square)

## 📌 Sobre

Lê um arquivo `.txt`, limpa o texto, conta quantas vezes cada palavra aparece e exibe um ranking com barrinhas no terminal. Projeto focado em manipulação de texto e estruturas de dados, sem biblioteca externa, tudo na mão.

## 🧠 O que eu aprendi e pratiquei aqui

- **Manipulação de strings:** Remover pontuação caractere por caractere com `string.punctuation`, normalizar com `.lower()` e tokenizar com `.split()`.
- **Dicionário como contador:** Implementei a contagem manualmente com `frequency[word] += 1` em vez de usar o `Counter` do `collections`. Mais verboso, mas ajuda a entender o que acontece por baixo.
- **Stopwords na raça:** Lista manual de palavras irrelevantes em português pra filtrar artigos e preposições antes de contar. Nada sofisticado, mas funciona pro propósito.
- **Ordenação com lambda:** Usar `sorted()` com `key=lambda item: item[1]` pra ordenar os pares `(palavra, contagem)` pelo valor.
- **Tratamento de erros:** `try/except` no `read_file` pra não quebrar quando o arquivo não existe ou tem algum problema de leitura.
- **Type hint:** Primeira vez usando `dict[str, int]` como anotação de tipo numa função. Pequeno, mas novo pra mim.
