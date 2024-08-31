# Análise de Dados de Vendas (Sales-Data-Analysis)

Este projeto realiza uma análise de dados de vendas utilizando uma base de dados real. Essa base foi obtida do [Kaggle](https://www.kaggle.com/datasets/beekiran/sales-data-analysis?resource=download), e alguns ajustes foram feitos para adequá-la às necessidades do projeto.

## Estrutura do Projeto

```
sales-data-analysis/
│
├── csv/
│   ├── vendas_1.csv
│   ├── vendas_2.csv
│   ├── ...
│   └── vendas_20.csv
│
├── env/
│
├── funcoes/
│   ├── analise.py
│   ├── visualizacao.py
│   ├── exportacao.py
│   ├── processamento.py
│   └── __init__.py
│
├── notebooks/
│   ├── sales_analysis_files.ipynb
│
├── resultados_analise/
│   ├── produtos_mais_vendidos.csv
│   ├── produtos_mais_vendidos.png
│   ├── total_vendas_por_regiao.csv
│   ├── total_vendas_por_regiao.png
│
├── main.py
├── README.md
└── requirements.txt

```

### Descrição dos Diretórios e Arquivos

- **`csv/`**: Contém os arquivos CSV que foram divididos a partir do dataset original do Kaggle. Esses arquivos são usados como entrada para o processamento e análise.
  - **`vendas_1.csv`** até **`vendas_20.csv`**: Partes do dataset original, divididas para simular a presença de múltiplos arquivos CSV.

- **`env/`**: Arquivos de dependências do ambiente virtual.

- **`funcoes/`**: Contém funções modulares para processamento, análise, visualização e exportação de dados.
  - **`analise.py`**: Contém funções para análise de dados (`calcular_total_vendas_por_regiao`, `identificar_produtos_mais_vendidos`).
  - **`visualizacao.py`**: Funções para criação de gráficos com Matplotlib e Seaborn.
  - **`exportacao.py`**: Funções para exportar resultados das análises para arquivos CSV.
  - **`processamento.py`**: Função para ler e combinar todos os arquivos CSV de um diretório.
  - **`__init__.py`**: Torna a pasta `funcoes` um pacote Python e facilita a importação de suas funções.

- **`notebooks/`**: Contém notebook Jupyter usado para ajustes no dataset original.
  - **`sales_analysis_files.ipynb`**: Notebook que foi utilizado para preparar o dataset original. Inclui a criação da coluna "Region" para categorizar as vendas por região nos Estados Unidos e a divisão do dataset em 20 partes.

- **`main.py`**: Script principal que orquestra a leitura dos dados, análise, visualização e exportação dos resultados.

- **`README.md`**: Documentação do projeto.

- **`requirements.txt`**: Lista de dependências necessárias para rodar o projeto.

## Preparação e Ajustes dos Dados

### Dataset Original

O dataset original foi obtido do [Kaggle](https://www.kaggle.com/datasets/beekiran/sales-data-analysis?resource=download) e contém informações detalhadas sobre vendas nos Estados Unidos.

### Ajustes Realizados

1. **Adição da Coluna "Region"**: Uma nova coluna chamada "Region" foi adicionada para categorizar as vendas por região dos Estados Unidos. Esse ajuste foi realizado diretamente no notebook Jupyter `sales_analysis_files.ipynb`.

2. **Divisão do Dataset**: O dataset ajustado foi dividido em 20 partes, cada um salvo como um arquivo CSV separado, para simular um cenário onde os dados estão distribuídos em múltiplos arquivos.

Os arquivos resultantes foram salvos no diretório `csv/`.

## Dependências

Para garantir que todas as dependências estão instaladas, é necessário criar e ativar um ambiente virtual Python. Use o comando abaixo para instalar as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Uso do Projeto

### 1. Configuração Inicial

1. Clone o repositório para sua máquina.
2. Navegue até o diretório do projeto.

### 2. Execução

#### Processamento e Análise de Dados

Execute o script `main.py` para processar os arquivos CSV de vendas, realizar a análise e exportar os resultados:

```bash
python main.py
```

### 3. Exportação dos Resultados

Os resultados da análise serão exportados para:

- **DataFrames (CSV):**
  - `total_vendas_por_regiao.csv`: Total de vendas por região.
  - `produtos_mais_vendidos.csv`: Produtos mais vendidos por receita.

- **Gráficos (PNG):**
  - `total_vendas_por_regiao.png`: Gráfico de barras mostrando o total de vendas por região.
  - `produtos_mais_vendidos.png`: Gráfico de barras mostrando os produtos mais vendidos.

Os arquivos exportados estarão no diretório: `\resultados_analise`.

## Funções e Documentação

As funções são documentadas com `docstrings`, facilitando a compreensão e manutenção do código.

### `processamento.py`

```python
def concatenar_csvs(diretorio: str) -> pd.DataFrame:
    """
    Lê e concatena todos os arquivos CSV de um diretório em um único DataFrame.
    
    Parâmetros:
    - diretorio: str, caminho do diretório onde estão os arquivos CSV
    
    Retorna:
    - DataFrame combinado contendo os dados de todos os arquivos CSV no diretório
    """
```

### `analise.py`

```python
def calcular_total_vendas_por_regiao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o total de vendas por região.
    
    Parâmetros:
    - df: DataFrame com os dados de vendas
    
    Retorna:
    - DataFrame com o total de vendas por região
    """
```

```python
def identificar_produtos_mais_vendidos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identifica os produtos mais vendidos com base na receita.
    
    Parâmetros:
    - df: DataFrame com os dados de vendas
    
    Retorna:
    - DataFrame com os produtos mais vendidos ordenados por receita
    """
```

### `visualizacao.py`

```python
def visualizar_dados(df: pd.DataFrame, diretorio_saida: str) -> None:
    """
    Cria visualizações das vendas por região e produtos mais vendidos e as exporta para arquivos de imagem.
    
    Parâmetros:
    - df: DataFrame com os dados de vendas
    - diretorio_saida: Caminho do diretório onde os gráficos serão salvos
    """
```

### `exportacao.py`

```python
def exportar_resultados(df_regiao: pd.DataFrame, df_produto: pd.DataFrame, diretorio_saida: str) -> None:
    """
    Exporta os resultados da análise para arquivos CSV.
    
    Parâmetros:
    - df_regiao: DataFrame com total de vendas por região
    - df_produto: DataFrame com produtos mais vendidos
    - diretorio_saida: Caminho do diretório para salvar os arquivos CSV
    """
```

## Boas Práticas e Eficiência

- **Modularidade:** O projeto é estruturado de maneira modular, com funções específicas separadas em arquivos distintos (`analise.py`, `visualizacao.py`, `processamento.py`). Isso torna o código mais reutilizável e fácil de manter.
- **Documentação:** Cada função é documentada com `docstrings`, descrevendo o propósito, parâmetros e retorno, facilitando a compreensão do código.
- **Reutilização de Código:** Funções como `concatenar_csvs`, `calcular_total_vendas_por_regiao`, e `visualizar_dados` podem ser facilmente reutilizadas em diferentes partes do projeto ou em outros projetos similares.
- **Uso de Bibliotecas:** O projeto utiliza bibliotecas como Pandas, Matplotlib e Seaborn para manipulação de dados e criação de gráficos, garantindo eficiência e clareza.

## Contribuição

Se você deseja contribuir para este projeto, faça um fork do repositório, crie um branch para suas alterações e envie um pull request. Todas as contribuições são bem-vindas!
