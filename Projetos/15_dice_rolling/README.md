# 🎲 Dice Roller — Dados no terminal com arte ASCII

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Stdlib](https://img.shields.io/badge/Stdlib-random-green?style=flat-square)
![Foco](https://img.shields.io/badge/Foco-Dicionários%20e%20ASCII-yellow?style=flat-square)

## 📌 Sobre

Simulador de dados no terminal com arte ASCII. Você escolhe quantos dados quer rolar (até 10), e eles aparecem lado a lado com os pontos certinhos, igualzinho aos dados de verdade. O projeto é simples mas o resultado visual ficou bem satisfatório, fiz acompanhando o nosso Deus Bro Code.

## 🧠 O que eu aprendi e pratiquei aqui

- **Dicionário como mapeamento:** Cada face do dado (1–6) mapeia pra uma tupla de 5 linhas ASCII. Foi a forma mais natural de organizar isso sem um monte de `if/elif`.
- **Renderização lado a lado:** O truque de imprimir linha por linha com `end=""` foi o que permitiu colocar os dados um ao lado do outro no terminal. Sem isso, cada dado apareceria empilhado.
- **`random.randint`:** Uso direto da stdlib pra simular o sorteio de cada dado.
- **Validação de input com `while True`:** Loop que só sai quando o usuário digita um valor válido (máximo 10 dados).

## ▶️ Como rodar

```bash
python main.py
```

```
Quantos dados?
> 3
┌─────────┐┌─────────┐┌─────────┐
│  ●      ││  ●   ●  ││    ●    │
│    ●    ││    ●    ││         │
│      ●  ││  ●   ●  ││    ●    │
└─────────┘└─────────┘└─────────┘

Total: 9
```

## ⚠️ Limitações

- [ ] Máximo de 10 dados (mais que isso quebra a formatação do terminal)
- [ ] Não valida se o input é um número inteiro (digitar letras quebra o código)
- [ ] Sem histórico de rodadas anteriores