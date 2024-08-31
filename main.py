from funcoes import concatenar_csvs, calcular_total_vendas_por_regiao, identificar_produtos_mais_vendidos, visualizar_dados, exportar_resultados
import pandas as pd

if __name__ == "__main__":
    diretorio_dados = 'csv'
    diretorio_saida = 'resultados_analise'
    
    # Leitura e combinação dos arquivos CSV
    df_completo = concatenar_csvs(diretorio_dados)

    # Análise dos dados
    df_total_vendas_regiao = calcular_total_vendas_por_regiao(df_completo)
    df_produtos_mais_vendidos = identificar_produtos_mais_vendidos(df_completo)
    
    # Visualização dos dados
    visualizar_dados(df_completo, diretorio_saida)
    
    # Exportação dos resultados
    exportar_resultados(df_total_vendas_regiao, df_produtos_mais_vendidos, diretorio_saida)