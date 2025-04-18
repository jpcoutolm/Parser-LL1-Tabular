# 📚 Analisador Sintático LL(1) com Visualização de Dados

Este projeto une a teoria da construção de analisadores sintáticos com a prática de análise de dados. O objetivo principal é implementar um **parser LL(1)** para uma gramática simples, mostrando seu funcionamento passo a passo. Além disso, uma aplicação web interativa foi desenvolvida com **Streamlit** para facilitar a visualização dos dados analisados a partir de arquivos CSV.

---

## 🧠 Analisador LL(1) Tabular

### 📌 Descrição
O analisador sintático descendente preditivo LL(1) foi construído com base em uma gramática simples que simula comandos condicionais. Ele usa uma **tabela de parsing**, **conjuntos FIRST e FOLLOW** e uma pilha para interpretar a entrada.

### 📖 Gramática utilizada
```
S → if E then S else S | a  
E → b | c
```

### 📋 Conjuntos FIRST e FOLLOW

- **FIRST(S)** = { if, a }
- **FOLLOW(S)** = { else, $ }
- **FIRST(E)** = { b, c }
- **FOLLOW(E)** = { then }

### 🧮 Tabela LL(1)
| Não-terminal | if | a | b | c | then | else | $ |
|--------------|----|---|---|---|------|------|---|
| S            | S → if E then S else S | S → a |   |   |      |      |   |
| E            |    |   | E → b | E → c |      |      |   |

### 🧰 Como Funciona o Código

O código simula o parsing de uma entrada como `if b then a else a $` utilizando uma pilha e consulta à tabela LL(1):

- Início com a pilha: `['$', 'S']`
- Para cada token da entrada, verifica o topo da pilha:
  - Se for terminal e coincidir com o token, desempilha e consome.
  - Se for não-terminal, usa a tabela para decidir a produção.
  - Se não encontrar produção válida, exibe erro.
- Aceitação ocorre se a pilha e entrada estiverem sincronizadas com `$`.

---

## 📊 Visualização com Streamlit

### 📌 Descrição

Para complementar a experiência, foi desenvolvida uma aplicação web com **Streamlit** que permite ao usuário fazer upload de um arquivo CSV e visualizar estatísticas básicas das colunas numéricas, além de gráficos interativos com Plotly.

### 🧰 Funcionalidades

- Upload de arquivos `.csv`
- Exibição prévia dos dados (DataFrame)
- Seleção de colunas numéricas
- Cálculo de:
  - Média
  - Mediana
  - Desvio padrão
- Geração de um histograma interativo

### ▶️ Como Executar

1. Instale as dependências:
```bash
pip install streamlit pandas plotly
```

2. Execute o app:
```bash
streamlit run nome_do_arquivo.py
```

> Substitua `nome_do_arquivo.py` por `430024b8-fa6c-4a7e-aade-ea4e89435a0a.py` ou renomeie conforme preferir.

---

## 👨‍🎓 Autor

**João Pedro do Couto**  
Estudante de Engenharia da Computação e Análise e Desenvolvimento de Sistemas  
GitHub: [@jpcoutolm](https://github.com/jpcoutolm)
