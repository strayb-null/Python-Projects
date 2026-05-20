# 🔐 Gerador de Senhas (Estudo de Segurança e CLI)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Foco](https://img.shields.io/badge/Foco-Estudo%20Prático-yellow?style=flat-square)
![Security](https://img.shields.io/badge/Security-CSPRNG-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=flat-square)


## 📌 Sobre
Este projeto começou como um exercício básico de terminal, mas evoluiu durante o estudo. A maioria dos tutoriais na internet ensina a gerar senhas usando o módulo `random`, mas descobri que ele é previsível e inseguro para criptografia. 

O objetivo aqui foi pegar a ideia original e refatorar aplicando conceitos de segurança real, tratamento de erros e sintaxe moderna do Python, transformando um script simples em algo mais robusto.

## 🧠 O que eu aprendi e pratiquei aqui
- **Segurança Real:** A diferença crucial entre `random` (pseudo-aleatório) e `secrets` (aleatoriedade criptográfica do sistema operacional).
- **Programação Defensiva:** Como usar `try/except` e loops `while` para impedir que o programa quebre quando o usuário digita letras em vez de números.
- **Sintaxe Moderna:** Uso do `match/case` (Python 3.10+) para deixar o menu de opções muito mais limpo do que uma escadinha de `if/elif`.
- **Matemática na Prática:** Como calcular a **Entropia** (a força real da senha em bits) usando a fórmula de Shannon (`math.log2`), em vez de apenas "chutar" se a senha é forte.
- **Organização:** Dividir o código em funções com responsabilidades únicas e usar *Type Hints* (`-> int`, `-> str`) para deixar o código mais legível.

## 🚀 Como rodar
Certifique-se de ter o Python 3.10 ou superior instalado (por causa do `match/case`).

```bash
cd 01_basico/12_gerador_senhas
python main.py