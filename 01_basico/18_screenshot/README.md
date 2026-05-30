# 📸 Screenshot Tool — Captura de tela com timestamp automático

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Libs](https://img.shields.io/badge/Libs-pyscreenshot%20%7C%20datetime%20%7C%20os-green?style=flat-square)
![Foco](https://img.shields.io/badge/Foco-Automa%C3%A7%C3%A3o%20e%20Arquivos-yellow?style=flat-square)

## 📌 Sobre

Ferramenta simples de captura de tela que salva automaticamente o screenshot com nome baseado na data e hora da captura. O projeto surgiu como exercício de automação e manipulação de arquivos em Python.

## 🧠 O que eu aprendi e pratiquei aqui

- **`os.makedirs()` com `exist_ok=True`:** Cria a pasta de destino caso ela não exista, sem lançar erro se já existir. Evita verificações manuais com `if os.path.exists()`.
- **`datetime.now().strftime()`:** Formata a data e hora atual como string pro nome do arquivo. Garante que cada screenshot tenha um nome único e organizado cronologicamente.
- **`pyscreenshot.grab()`:** Captura o estado atual da tela inteira e retorna um objeto de imagem compatível com Pillow, que pode ser salvo diretamente com `.save()`.
- **Organização de saída:** Salvar arquivos em subpastas dedicadas (`screenshots/`) é uma boa prática pra não poluir o diretório raiz do projeto.

## ⚠️ Limitações

- [ ] Não suporta captura de região específica da tela
- [ ] Não possui delay configurável antes da captura
- [ ] Não abre a imagem automaticamente após salvar
- [ ] Não possui menu interativo no terminal