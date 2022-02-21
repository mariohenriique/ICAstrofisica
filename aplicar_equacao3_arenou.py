from alterar_nome_colunas import escrever_csv

import criar_df

import pandas as pd

print('começando')

for i in range(len(criar_df.df_test['nomedoarquivo'])):
    num = i
    localarquivo = criar_df.df_test.nomedoarquivo.iloc[num] + '/CSV/' + criar_df.df_test.nomedoarquivo.iloc[num] + '_filtro_renomeado'

    aglomerado = pd.read_csv(localarquivo)

    #transformar o arquivo em um dataframe
    parametro = pd.DataFrame(aglomerado)

    filtro_arenou3 = parametro[parametro['Nper'] > 8]

    localarquivofinal = criar_df.df_test.nomedoarquivo.iloc[num] + '/CSV/' + criar_df.df_test.nomedoarquivo.iloc[num] + '_filtro3_arenou'

    csv = escrever_csv(localarquivofinal,filtro_arenou3)
    print(localarquivofinal + ' ok')