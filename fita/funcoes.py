import os
import sys
from terminal import ok,aviso,erro

def obter_pasta_base():
    """
    Retorna a pasta base do sistema.
        Quando roda pelo Python:
            C:/Users/wandersoncop/Desktop/auto_fita_espelho
    Quando roda pelo EXE:
            pasta onde está o auto_fita.exe.
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)

    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def localizar_arquivo_fita():
    """
    Procura o arquivo da Fita Espelho dentro da pasta Entrada.
        Retorna:
            caminho_arquivo: caminho completo do arquivo encontrado
            arquivo_encontrado: nome do arquivo encontrado
            diretorio: caminho da pasta Entrada
    """

    diretorio = os.path.join(
        obter_pasta_base(),
        "Entrada"
    )
    # Cria a pasta Entrada caso ela não exista
    os.makedirs(diretorio,exist_ok=True)

    arquivo_encontrado = None

    for arquivo in os.listdir(diretorio):
        if (
            arquivo.lower().startswith("fita_servidor_")
            and arquivo.lower().endswith(".txt")
        ):
            arquivo_encontrado = arquivo
            break
    if arquivo_encontrado:
        caminho_arquivo = os.path.join(
            diretorio,
            arquivo_encontrado
        )
    else:
        caminho_arquivo = None

    return caminho_arquivo, arquivo_encontrado, diretorio

