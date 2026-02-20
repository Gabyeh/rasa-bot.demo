# rasa-bot.demo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Gabyeh/rasa-bot.demo/HEAD)

Usuário: Quero calcular o preço de um produto
Bot: Qual é o custo base do produto?
Usuário: 100
Bot: Qual o percentual de custos operacionais?
Usuário: 10
Bot: Qual o percentual de impostos?
Usuário: 15
Bot: Qual a margem de lucro desejada?
Usuário: 20
Bot: O preço final do produto é R$ 153,85

# Rasa Bot – Cálculo de Preço com Markup

Este projeto é um chatbot desenvolvido com Rasa para calcular o preço final de um produto
utilizando a metodologia de markup.

O bot solicita ao usuário:
- Custo base do produto
- Percentual de custos operacionais
- Percentual de impostos
- Margem de lucro desejada
- Percentual de desconto (opcional)

Ao final, retorna o preço final calculado.

## 🧠 Objetivo do projeto
Projeto desenvolvido para fins de estudo e prática em:
- Python
- Rasa Framework
- Lógica de negócios (formação de preços)
- Versionamento com Git e GitHub

## ⚙️ Tecnologias utilizadas
- Python 3.8
- Rasa Open Source
- Rasa SDK

## ▶️ Como executar (ambiente local)
> Observação: este projeto foi desenvolvido e testado com **Python 3.8**.

```bash
pip install rasa 
rasa train
rasa shell
