import os
import pandas as pd

def concatenar_csvs(diretorio: str):
    """
    Lê e concatena todos os arquivos CSV de um diretório em um único DataFrame.
    
    Parâmetros:
    - diretorio: str, caminho do diretório onde estão os arquivos CSV
    
    Retorna:
    - DataFrame combinado contendo os dados de todos os arquivos CSV no diretório
    """
    # Lista todos os arquivos CSV no diretório
    arquivos_csv = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith('.csv')]
    
    # Lê e concatena todos os arquivos CSV em um único DataFrame
    df_completo = pd.concat([pd.read_csv(arquivo) for arquivo in arquivos_csv], ignore_index=True)
    
    return df_completo
