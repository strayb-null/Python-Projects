# 🧾 Gerador de Recibo em PDF (Estudo com ReportLab)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Experimento-yellow?style=flat-square)

## 📌 Sobre
Um script simples e experimental criado para estudar a biblioteca `ReportLab` e entender como gerar PDFs via código Python. 

Este projeto é apenas um exercício prático para brincar com layout, tabelas e cores. Os dados estão "chumbados" (hardcodados) no código e não há integração com banco de dados ou sistemas de pagamento reais.

## 🚀 Funcionalidades
- 📄 Geração de um PDF com um layout organizado (cabeçalho, dados, tabela e rodapé).
- 🎨 Cores customizadas (`HexColor`) e estilos de texto.
- 📊 Criação de tabelas com formatação manual (cores alternadas, bordas e alinhamentos).
- 📅 Inserção automática da data de hoje (a única coisa realmente dinâmica no código).

## 🛠️ Conceitos Explorados (Nível de Estudo)
- **Montagem de PDF (Platypus):** Entendimento básico de como usar o `SimpleDocTemplate` e empilhar elementos (*flowables* como `Paragraph`, `Table`, `Spacer`) numa lista `story` para montar a página.
- **Estilização na Mão:** Aprender a configurar `TableStyle` e `ParagraphStyle` via código, percebendo na prática como é verboso fazer layout de PDF sem usar HTML/CSS.
- **Limitações do Escopo:** O código não possui tratamento de erros, logs, ou leitura de dados externos. O foco foi puramente entender a renderização visual da biblioteca.
