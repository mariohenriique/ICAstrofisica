import muda_csv

import pandas as pd

import criar_df

def escrever_csv(onde,df):
    with open(onde,'w') as arquivo:
        arquivo.write('# ')
        df.to_csv(arquivo)

for i in range(len(criar_df.df_test['nomedoarquivo'])):
    num = i
    #criar uma variavel e usar o pandas para ler o arquivo
    localarquivo = criar_df.df_test.nomedoarquivo.iloc[num] + '/CSV/' + criar_df.df_test.nomedoarquivo.iloc[num] + '_csv'
    aglomerados = pd.read_csv(localarquivo)

    #transformar o arquivo em um dataframe
    parametro = pd.DataFrame(aglomerados)

    parametro = parametro.rename(columns={'BP-RP':'bp_rp','E(BP-RP)':'phot_bp_rp_excess_factor'})

    localarquivofinal = criar_df.df_test.nomedoarquivo.iloc[num] + '/CSV/' + criar_df.df_test.nomedoarquivo.iloc[num] + '_filtro_renomeado'

    csv = escrever_csv(localarquivofinal,parametro)
    print(localarquivofinal + ' ok')