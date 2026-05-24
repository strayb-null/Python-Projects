# 🎮 2048 — Porque todo mundo precisa reinventar a roda pelo menos uma vez

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Pygame](https://img.shields.io/badge/Pygame-2.x-orange?style=flat-square)
![Foco](https://img.shields.io/badge/Foco-Lógica%20de%20Jogo-yellow?style=flat-square)

## 📌 Sobre

O clássico 2048 feito com Pygame. Esse foi o projeto que mais precisei recorrer a referências externas a lógica de movimento e merge dos tiles me deu mais trabalho do que esperava. Segui o vídeo do [Tech With Tim](https://www.youtube.com/@TechWithTim) para me ajudar a entender algumas coisas, na real varias coisas :P


## 🧠 O que eu aprendi e pratiquei aqui

- **Pygame na prática:** Renderização de frames, event loop, controle de FPS e como desenhar coisas na tela sem querer explodir o computador.
- **Lógica de movimento:** A parte mais difícil do projeto. Cada direção tem um comportamento diferente e foi preciso abstrair isso em lambdas pra não repetir código quatro vezes. Ficou estranho mas funcionou.
- **Animação frame a frame:** Os tiles se movem suavemente usando `MOVE_VEL` por frame. Parece trivial, mas sincronizar o movimento com a lógica de merge deu bastante trabalho.
- **Dicionário como grade:** Em vez de uma matriz 2D, a grade usa um `dict` com chave `"rowcol"` (ex: `"23"`). Simples e eficiente pra checar colisões e posições.
- **Lambdas pra generalização:** Toda a lógica de direção (left, right, up, down) usa funções lambda pra evitar repetição. Foi a minha primeira vez usando esse padrão e faz sentido depois que você entende.


## ⚠️ Estado atual

O jogo funciona, mas ainda tá incompleto. Falta:

- [ ] Tela de game over de verdade (hoje só printa "lost" internamente)
- [ ] Contador de pontuação
- [ ] Tela de vitória quando chegar no 2048
- [ ] Talvez um restart sem fechar o programa

