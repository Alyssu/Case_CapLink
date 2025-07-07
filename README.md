<h2 align="center">Case CapLink</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Resolução Case CapLink - Pessoa Estagiária de Automação de Processos e Dados
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 Sobre o projeto <a name = "about"></a>

Esse pequeno projeto tem por função resolver o case proposto no Processo Seletivo da CapLink para Pessoa Estagiária de Automação de Processos e Dados.

A ideia central consiste na implementação de uma pequena automação, com o objetivo de avaliar as capacidades em:
- Consumir uma API e fazer requisições GET/POST
- Manipular e processar dados
- Resolução de problemas
- Documentação e estruturação de fluxo

## 🏁 Preparação do Ambiente <a name = "getting_started"></a>

Para iniciar o projeto, basta fazer o download do arquivo ou clonar o repositorio em sua máquina atraves do comando Git
```
git clone https://github.com/Alyssu/Case_CapLink.git
```

Após o download/clonagem do repositorio, basta seguir as instruções abaixo

### Pre requisitos

Ao abrir o projeto, inicie o arquivo 'requeriments.bat'

Ou, digite o seguinte codigo no terminal

```
pip install -r requiriments.txt
```

## 🔧 Rodando o Programa <a name = "tests"></a>

Depois de ter instalado as dependencias, o programa já está pronto para rodar.

### Faça a inicialização do arquivo main.py

Após rodar o programa, deverá aparecer o seguinte resultado no terminal:

```
--- Relatório de Atividade dos Usuários ---
ID | Nome do Usuario | Qtd. Posts | Media de Caracteres
--------------------------------------------------------------------------------
1 | Leanne Graham | 10 | 164.5
2 | Ervin Howell | 10 | 162.9
3 | Clementine Bauch | 10 | 153.8
4 | Patricia Lebsack | 10 | 182.3
5 | Chelsey Dietrich | 10 | 162.5
6 | Mrs. Dennis Schulist | 10 | 147.0
7 | Kurtis Weissnat | 10 | 163.5
8 | Nicholas Runolfsdottir V | 10 | 160.6
9 | Glenna Reichert | 10 | 154.6
10 | Clementina DuBuque | 10 | 154.7
```

#### Correndo tudo bem, será gerado um relatorio em formato CSV

#### E será feito um POST para o caminho ficcticio /send-email
```
Relatório salvo com sucesso em 'relatorio_usuarios.csv'

Simulando envio do relatório para o destinatário: {destinatário}
```

## ⛏️ Ferramentas Utilizadas <a name = "built_using"></a>

- [Python](https://www.python.org/) - Linguagem Usada
- [Requests](https://pypi.org/project/requests/) - Biblioteca para requisições HTTP
- [JSON](https://docs.python.org/pt-br/3.13/library/json.html) - Biblioteca para manipulação de JSON's em Python
- [{JSON} Placeholder](https://vuejs.org/) - API para extração dos dados
- [CSV](https://docs.python.org/pt-br/3/library/csv.html) - Biblioteca para leitura e escrita de arquivos CSV

## ✍️ Authors <a name = "authors"></a>

- [@Alyssu](https://github.com/Alyssu) - Ideia & Realização

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
