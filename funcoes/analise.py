import pandas as pd

def calcular_total_vendas_por_regiao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o total de vendas por região.
    """
    df.groupby("Region")["Sales"].sum().reset_index()


def identificar_produtos_mais_vendidos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identifica os produtos mais vendidos com base na receita.
    """
    df.groupby("Product")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)