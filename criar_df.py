import pandas as pd

arquivo = pd.read_csv('parametro_para_rodar_programa.txt')

df_test = pd.DataFrame(arquivo)

df_test = df_test.rename(columns={'#Name': 'nomedoarquivo'})

df_test.head()
