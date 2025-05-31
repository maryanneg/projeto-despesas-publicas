![image](https://github.com/user-attachments/assets/310b221d-988b-479e-b49a-ca3cca8754bb)

# Projeto de Análise de Despesas Públicas - 2024

Este projeto faz parte da disciplina de TÓPICOS DE BIG DATA EM PYTHON tem como objetivo baixar, extrair e analisar dados de despesas públicas do Portal da Transparência do governo federal brasileiro para o ano de 2024. A análise inclui total de gastos, distribuição mensal, gastos por órgãos superiores e análise regional por Unidade da Federação (UF) com a dashboard em Excel completa para facilitar a visualização e exploração dos dados.


## Funcionalidades

- Download automático dos arquivos zip com dados mensais de despesas públicas.
- Extração e armazenamento dos dados em formato CSV.
- Análise consolidada dos dados com:
- Dashboard em Excel para visualização interativa dos dados.


## Estrutura do Projeto

-`python - captando dados` -  Pasta com script em python que capta dados do portal da transparência 
- `dados_despesa/` — Pasta onde os arquivos CSV extraídos são salvos.
- Arquivo `dashboard_despesas.xlsx` — Dashboard em Excel com gráficos e tabelas dinâmicas.

---

## Como usar

1. Execute o bloco de código para baixar e extrair os arquivos, selecionando o ano (ex: 2024) e mês (ou todos).
2. Após o download
3. Abra o arquivo Excel `dashboard_despesas.xlsx` para uma análise interativa adicional.


## Observações
- Os dados são obtidos diretamente do Portal da Transparência.
- Certifique-se de ter conexão com a internet para o download dos dados.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pandas`
  - `matplotlib`
  - `requests`
  -` zipfile`
- Microsoft Excel (ou software compatível) para a dashboard

Para instalar as bibliotecas necessárias, execute:

```bash
pip install pandas matplotlib ipywidgets requests
