# 🔁 Palindrome Checker — Quatro formas de resolver o mesmo problema

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Stdlib](https://img.shields.io/badge/Stdlib-built--in-green?style=flat-square)
![Foco](https://img.shields.io/badge/Foco-Strings%20e%20Algoritmos-yellow?style=flat-square)

## 📌 Sobre

Verificador de palíndromos implementado de quatro formas diferentes. O projeto surgiu enquanto estudava manipulação de strings em Python, e percebi que comparar abordagens distintas pro mesmo problema é uma das melhores formas de entender o que está acontecendo por baixo dos panos.

## 🧠 O que eu aprendi e pratiquei aqui

- **Índices negativos:** `s[-i-1]` acessa a string de trás pra frente sem precisar criar nenhuma cópia. Entender que `s[-1]` é o último caractere e que isso pode ser combinado com um índice variável foi o clique principal.
- **Two Pointers:** Técnica clássica de algoritmos onde dois ponteiros caminham das extremidades em direção ao centro. Mais eficiente porque para assim que encontra o primeiro erro.
- **Divisão inteira `//`:** Usada pra percorrer só a metade da string. O `//` garante que strings ímpares não causem erro — o caractere do centro é ignorado automaticamente.
- **Slicing com passo negativo `[::-1]`:** Forma mais pythônica de inverter uma string, mas a única que cria uma cópia na memória — o que a torna menos eficiente pra strings muito grandes.
- **`all()` com generator expression:** Combina verificação de todas as posições numa única linha sem criar listas intermediárias. Elegante e eficiente.
- **`reversed()` + `join()`:** Abordagem mais explícita que o slicing, mas igualmente cria uma cópia da string invertida antes de comparar.

## 🔀 Os quatro métodos

| Método | Cria cópia? | Para cedo em caso de erro? |
|---|---|---|
| `two_pointers` | ❌ | ✅ |
| `using_all` | ❌ | ✅ |
| `using_slicing` | ✅ | ❌ |
| `using_reversed` | ✅ | ❌ |

## ⚠️ Limitações

- [ ] Não ignora espaços e pontuação (`"A man a plan a canal Panama"` retorna falso)
- [ ] Não normaliza maiúsculas (`"Madam"` retorna falso)
- [ ] Não suporta caracteres acentuados (`"ala"` funciona, `"ímã"` pode gerar comportamento inesperado)