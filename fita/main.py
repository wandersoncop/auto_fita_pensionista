import os
import pandas as pd

from terminal import ok,aviso,erro,info
from funcoes import(
    localizar_arquivo_fita,
    extrair_tipo_0,
    extrair_tipo_9,
    ler_fita_por_tipo,
    formatar_data

)

from mapeamentos import (
    # LAYOUT_TIPO_ são as posições na fita ex:'SIAPE': (9, 16),
    # HEADER_TIPO_ faz a sequencia desejada
    # CAMPOS_DATA aqui é  lista de campos de data que serão formatados pela função formatar_data
    LAYOUT_TIPO_1,
    HEADER_TIPO_1,
    # LAYOUT_TIPO_2,
    # HEADER_TIPO_2,
    # LAYOUT_TIPO_3,
    # LAYOUT_TIPO_4,
    # HEADER_TIPO_4,
    # LAYOUT_TIPO_5,
    # HEADER_TIPO_5,
    # LAYOUT_TIPO_6,
    # HEADER_TIPO_6,
    CAMPOS_DATA
)


def main():

    caminho_arquivo, arquivo_encontrado, diretorio = localizar_arquivo_fita()

    if caminho_arquivo and os.path.exists(caminho_arquivo):

        ok(f" Arquivo encontrado:{arquivo_encontrado}")

        # ====================================================================
        # TIPO 0 - MesFita
        # ====================================================================

        Mesfita = extrair_tipo_0(caminho_arquivo)
        info(f'Mês da Fita: {Mesfita}')
        
        # ====================================================================
        # TIPO 9 - PARA VALIDAÇÃO DA QUANTIDADE DE REGISTROS DO MesFita
        # ====================================================================

        total_registros = extrair_tipo_9(caminho_arquivo)
        info(f'Total de regitros:{total_registros}')
        print()

        # ====================================================================
        # TIPO 1 - Dados cadastrais instituidor falecido
        # ====================================================================
        # extração e estruturação dos dados

        registros_tipo_1 = ler_fita_por_tipo(
            caminho_arquivo,# onde esta o arquivo
            LAYOUT_TIPO_1, 
            '1',                # tipo do arquivo ex:tipo_1,tipo_2,tipo_3....
            CAMPOS_DATA,
                    # mapas_auxiliares,   # é o dicionario para configuracao dos novos campos
        )
        # print(registros_tipo_1 )
        df_instituidor_falecido = pd.DataFrame(registros_tipo_1)

        
        # print(df_instituidor_falecido["Data_exclusao_instituidor"].head(10))

        df_instituidor_falecido.to_excel(
            'instituidor_falecido.xlsx',
            index=False
        )



    else:
        erro('Arquivo fita_pensao não encontrado')
        print()
        info(f'Pasta esperada:{diretorio}')
        print()
        aviso("Copie o arquivo fita_pensionista_AAAA_MM.txt para a pasta Entrada.")
        print()
        return False





if __name__=='__main__':
    main()           # lista de campos que são data
  