import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .analise import calcular_total_vendas_por_regiao, identificar_produtos_mais_vendidos
import os

def visualizar_dados(df: pd.DataFrame, diretorio_saida: str):
    """
    Cria gráficos das vendas por região e produtos mais vendidos e exporta para arquivos de imagem.
    
    Parâmetros:
    - df: DataFrame com os dados de vendas
    - diretorio_saida: Caminho do diretório onde os gráficos serão salvos
    """
    os.makedirs(diretorio_saida, exist_ok=True)

    # Total de vendas por região
    total_vendas_regiao = calcular_total_vendas_por_regiao(df)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Region', y='Sales', data=total_vendas_regiao)
    plt.title('Total de Vendas por Região')
    plt.savefig(os.path.join(diretorio_saida, 'total_vendas_por_regiao.png'))  
    plt.show()
    
    # Produtos mais vendidos
    produtos_mais_vendidos = identificar_produtos_mais_vendidos(df)
    plt.figure(figsize=(10, 6))
    sns.barplot(y='Product', x='Sales', data=produtos_mais_vendidos, orient='h')
    plt.title('Produtos Mais Vendidos')
    plt.savefig(os.path.join(diretorio_saida, 'produtos_mais_vendidos.png'))
    plt.show()
