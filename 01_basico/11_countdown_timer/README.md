# ⏱️ Timer Regressivo no Terminal (Estudo de CLI e Manipulação de Tempo)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![CLI](https://img.shields.io/badge/Interface-Terminal-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Experimento-yellow?style=flat-square)

## 📌 Sobre
Um script simples e experimental criado para estudar manipulação de tempo, formatação de strings e controle de saída no terminal Python. 

Este projeto é apenas um exercício prático para brincar com interfaces de linha de comando (CLI) dinâmicas e validação de dados. O código não possui interface gráfica (GUI), notificações de sistema ou opções de pausar/retomar, focando puramente na lógica de contagem e interação básica com o usuário.

## 🚀 Funcionalidades
- ⏳ Contagem regressiva visual diretamente no terminal.
- 🔄 Atualização dinâmica na mesma linha (usando `\r` para não poluir o terminal com múltiplas linhas de impressão).
- 🛡️ Validação de entrada (bloqueia textos e números negativos, forçando o usuário a digitar um valor válido).
- ⏱️ Formatação automática de segundos para o padrão `MM:SS`.
- 💥 Mensagem de encerramento customizada ("Bazinga") ao finalizar o tempo.

## 🛠️ Conceitos Explorados (Nível de Estudo)
- **Controle de Fluxo e Input:** Entendimento prático de como usar `while True` com `break`, `continue` e blocos `try/except` (`ValueError`) para criar um loop de validação de input à prova de falhas básicas do usuário.
- **Manipulação do Terminal:** Aprender a usar o parâmetro `end='\r'` na função `print()` para sobrescrever a linha atual (carriage return), simulando uma interface dinâmica sem precisar de bibliotecas externas como `curses` ou `rich`.
- **Matemática e Tempo:** Uso da função nativa `divmod()` para converter segundos em minutos e segundos de forma limpa e pitônica, combinado com `time.sleep(1)` para controlar o ritmo da execução.
- **Limitações do Escopo:** O script bloqueia a thread principal (não é assíncrono), não permite cancelar a contagem (ex: via `KeyboardInterrupt` tratado) e depende de o terminal do usuário suportar o caractere de retorno de carro (`\r`) corretamente.