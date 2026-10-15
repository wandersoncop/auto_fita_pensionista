import os

from terminal import ok,aviso,erro,info
from funcoes import(
    localizar_arquivo_fita
)



def main():

    caminho_arquivo, arquivo_encontrado, diretorio = localizar_arquivo_fita()

    if caminho_arquivo and os.path.exists(caminho_arquivo):

        print(f" Arquivo encontrado:{arquivo_encontrado}")
        print()
    else:
        erro('Arquivo fita pensionista não encontrado')
        print()
        info(f'Pasta esperada:{diretorio}')
        print()
        aviso("Copie o arquivo fita_pensionista_AAAA_MM.txt para a pasta Entrada.")
        print()
        return False




if __name__=='__main__':
    main()    