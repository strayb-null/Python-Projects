# 🔐 Cifra de César — Criptografia clássica em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Stdlib](https://img.shields.io/badge/Stdlib-string-green?style=flat-square)
![Foco](https://img.shields.io/badge/Foco-Lógica%20e%20Módulos-yellow?style=flat-square)

## 📌 Sobre

Implementação da Cifra de César — um dos algoritmos de criptografia mais antigos do mundo. O projeto surgiu enquanto estudava, e percebi que a cifra é um bom exemplo pra consolidar alguns conceitos na prática.

## 🧠 O que eu aprendi e pratiquei aqui

- **Operador módulo `%`:** O coração da cifra. Sem ele o índice ultrapassa o alfabeto e o código quebra. Entender que `28 % 26 = 2` é o mesmo que "deu uma volta completa e sobrou 2" foi o clique que faltava.
- **Separação de responsabilidades:** A lógica da cifra vive em `cipher.py` e a interface em `main.py`. Qualquer arquivo pode importar `cifrar()` sem efeitos colaterais.
- **Type hints e docstrings:** Primeiro projeto onde documentei a função no padrão Google Style com `Args`, `Returns` e `Example`.
- **`if __name__ == "__main__"`:** Entendi na prática por que esse padrão existe — sem ele, importar o módulo dispararia código indesejado.
- **Tratamento de erros:** Uso de `try/except ValueError` pra lidar com entrada inválida do usuário de forma elegante.


## ⚠️ Limitações

- [ ] Não suporta letras maiúsculas (normaliza tudo pra minúsculo)
- [ ] Não suporta caracteres acentuados (á, é, ç...)
- [ ] Chave limitada a 1–26 (poderia aceitar qualquer inteiro)