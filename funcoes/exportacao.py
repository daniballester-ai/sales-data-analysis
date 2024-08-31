import pandas as pd
import os

def exportar_resultados(df_regiao: pd.DataFrame, df_produto: pd.DataFrame, diretorio_saida: str):
    """
    Exporta os resultados da análise para arquivos CSV.
    """
    os.makedirs(diretorio_saida, exist_ok=True)
    df_regiao.to_csv(os.path.join(diretorio_saida, 'total_vendas_por_regiao.csv'), index=False)
    df_produto.to_csv(os.path.join(diretorio_saida, 'produtos_mais_vendidos.csv'), index=False)
