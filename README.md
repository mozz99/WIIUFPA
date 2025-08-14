# Análise de Canal para a Frequência de 3,5 GHz em Ambientes Fechados em pequena e larga escala usando Wireless Insite e Medições

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)

## 📖 Resumo
Este repositório contém os dados e códigos do trabalho de Análise de Canal para a Frequência de 3,5 GHz em Ambientes Fechados, que combina simulações computacionais e medições de campo. O projeto utiliza o software Wireless InSite (WI) para realizar uma análise de canal em pequena e larga escala, validando os resultados com uma campanha de medição realizada em um ambiente real.

O objetivo principal é caracterizar a propagação do sinal em 3,5 GHz, uma faixa crucial para sistemas 5G, dentro de edificações. O estudo compara os dados simulados com os medidos, valida o modelo computacional através do RMSE (Root Mean Squared Error) e, a partir disso, extrai parâmetros de pequena escala como Power Delay Profile, espalhamento de retardo e banda de coerência. Adicionalmente, explora-se o uso de uma rede neural para prever a potência recebida.

## 📝 Contexto e Motivação
Este trabalho foi desenvolvido no âmbito das pesquisas em radiopropagação da Universidade Federal do Pará (UFPA).

Título do Trabalho: Análise de Canal para a Frequência de 3,5 GHz em Ambientes Fechados em pequena e larga escala usando Wireless Insite e Medições.

-  **Autor:** Mozart Lima Malaquias Junior

-  **Instituição:** Universidade Federal do Pará

- **Local:** Belém

-  **Ano:** 2025

A motivação do projeto é a crescente demanda por conectividade de alta performance em ambientes internos (indoor), especialmente com a implementação de redes 5G. A frequência de 3,5 GHz é fundamental para essa tecnologia, mas sua propagação em ambientes fechados é complexa. Este estudo busca fornecer um modelo validado e uma análise detalhada que possam auxiliar no planejamento e otimização de redes de comunicação sem fio.

## 🚀 Metodologia e Abordagem
A metodologia do projeto é dividida em três etapas principais:

1. Campanha de Medição: Foram realizadas medições no térreo e no primeiro andar do prédio anexo dos Laboratórios de Engenharia Elétrica da UFPA.

2. Antenas: Omnidirecionais, desenvolvidas localmente.

3. Potência de Transmissão: 20 dBm.

4. Equipamento de Medição: Analisador de espectro ZPH Site Master da Rohde & Schwartz.

5. Simulação e Validação: O ambiente de medição foi recriado virtualmente no software de simulação por traçamento de raios Wireless InSite.

6. Os modelos de perda de percurso Floating-Intercept (FI) e Close-In (CI) foram aplicados.

7. A validação foi feita comparando os resultados simulados com os medidos, alcançando um RMSE de 3,681 dB para o térreo e 6,059 dB para o primeiro andar.

8. Análise e Predição: Com o modelo de simulação validado, foram extraídos parâmetros de pequena escala para caracterizar o canal. Além disso, foi proposto um modelo de rede neural para prever a potência de recepção em diferentes pontos.

## 📂 Estrutura do Repositório
```
.
├── wireless_insite_files/ # Arquivos de projeto e resultados da simulação
├── python/                 # Scripts em Python para análise e rede neural
│   ├── main.py
│   ├── analysis.py
│   └── neural_network.py
├── data/                   # Dados brutos e processados das medições de campo
├── paper/                  # Rascunhos e versão final do artigo/trabalho
├── .gitignore
└── README.md
```
## 💻 Instalação e Uso
Os códigos de análise de dados e o modelo de rede neural estão na pasta python/. Para executá-los, siga os passos:

1. Clone o repositório:

Bash

git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio
Crie e ative um ambiente virtual (recomendado):

Bash

2. python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:
(Um arquivo requirements.txt deverá ser criado na pasta python/)

Bash

3. pip install -r python/requirements.txt
Execute o script principal:

Bash

python python/main.py
🔧 Ferramentas e Tecnologias
-  **Wireless InSite:** Utilizado para a simulação de propagação por traçamento de raios.

-  **Python:** Linguagem principal para análise de dados, visualização e machine learning.

-  **NumPy & Pandas:** Para manipulação de dados numéricos e tabulares.

-  **Matplotlib / Seaborn:** Para a visualização de dados e geração de gráficos.

-  **Scikit-learn / TensorFlow / PyTorch:** Para a implementação do modelo de rede neural.

## 🤝 Como Contribuir
Contribuições são bem-vindas! Se você tiver sugestões para melhorar os modelos ou o código, sinta-se à vontade para:

1. Fazer um Fork deste repositório.

2. Criar uma nova Branch (git checkout -b feature/sua-feature).

3. Fazer o Commit de suas alterações (git commit -m 'Adiciona nova feature').

4. Fazer o Push para a Branch (git push origin feature/sua-feature).

5. Abrir um Pull Request.

## ✒️ Citação
Se você utilizar este trabalho em sua pesquisa, por favor, cite-o.
```
bibtex
@mastersthesis{malaquias2025analise,
  title     = {An{\'a}lise de Canal para a Frequ{\^e}ncia de 3,5 GHz em Ambientes Fechados em pequena e larga escala usando Wireless        Insite e Medi{\c{c}}{\~o}es},
  author    = {Malaquias Junior, Mozart Lima},
  school    = {Universidade Federal do Par{\'a}},
  year      = {2025},
  address   = {Bel{\'e}m}
}
```

## 📜 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
