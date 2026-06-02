# 🌐 09 - Fun Fact Generator (Web App)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)
![PyWebIO](https://img.shields.io/badge/PyWebIO-Interface-green?style=flat-square)
![API](https://img.shields.io/badge/REST_API-JSON-orange?style=flat-square)

## 📌 Sobre
Um aplicativo web simples que consome uma API externa de curiosidades inúteis (Useless Facts) e as exibe em uma interface interativa no navegador. 

O foco deste projeto foi sair do terminal, entender o ciclo de vida de uma requisição web e aplicar boas práticas de **resiliência e tratamento de erros**.

## 🚀 Funcionalidades
- 🔄 Consumo de API REST (GET) e parsing de JSON.
- 🖥️ Interface web interativa sem escrever HTML/CSS (usando PyWebIO).
- 🛡️ Tratamento robusto de erros de rede e HTTP (404, 500, 429, Timeout).
- ⏳ Feedback visual de carregamento (UX) para evitar telas em branco.

## 🛠️ Conceitos de Engenharia Aplicados
- **Separação de Responsabilidades:** A lógica de negócios (buscar dados) foi isolada da interface (renderizar botões).
- **Resiliência:** Uso de `try/except` combinado com `raise_for_status()` para capturar falhas de infraestrutura e do servidor.
- **UX (Experiência do Usuário):** Implementação de estados de "carregando" e mensagens de erro amigáveis.
