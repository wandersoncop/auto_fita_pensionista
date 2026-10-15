import os
import sys
from terminal import ok,aviso,erro

def obter_pasta_base():
    """
    Retorna a pasta base do sistema.
        Quando roda pelo Python:
            C:/Users/wandersoncop/Desktop/auto_fita_penionista
    Quando roda pelo EXE:
            pasta onde está o auto_fita.exe.
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)

    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def localizar_arquivo_fita():
    """
    Procura o arquivo da Fita pensionista dentro da pasta Entrada.
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
            arquivo.lower().startswith("fita_pensao_")
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

def extrair_tipo_0(caminho_arquivo):
    """Extrai o mês da fita."""

    with open(caminho_arquivo, encoding='latin-1') as arquivo_txt:

        for linha in arquivo_txt:

            if len(linha) > 25 and linha[24] == '0':
                ano = linha[52:56]
                mes = linha[56:60]

                return f"{ano}_{mes}"
    return "0000_00"

def extrair_tipo_9(caminho_arquivo):
    """
    Extrai do o quantitativo de registros do arquivo txt da fita
    que fica na ultima linha
    """
    with open(caminho_arquivo,encoding='latin-1') as arquivo_txt:
        for linha in arquivo_txt:
            if len(linha) > 25 and linha[24] == '9':
                return int(linha.strip()[-7:])
    return 0  

def extrair_tipos(linha,layout,campos_data=None, mapas_auxiliares=None):
    """Traduz cada linha da fita espelho usando as posições existentes no layout."""
    if campos_data is None:
        campos_data = []
    if mapas_auxiliares is None:
        mapas_auxiliares = {}
    registro = {}#cria um dicionario vazio para guardar o resultado
                  #quando percorre o layout coloca o valor da linha EX na fita:
                  #"CodEstadoCiv":(161,162)
                  #valor = linha[161:162].strip()
                  #valor = '1'     
    for nome_campo,posicoes in layout.items():
        inicio,fim = posicoes
        valor = linha[inicio:fim].strip()
        if nome_campo in campos_data:
            valor = formatar_data(valor)
        registro[nome_campo] = valor
    return registro    

def ler_fita_por_tipo(caminho_arquivo,layout,tipo_registro,campos_data=None,mapas_auxiliares=None):
    """Lê os registros da fita e os separa por tipo."""

    registros = []

    with open(caminho_arquivo, encoding='latin-1') as arquivo_txt:
        for linha in arquivo_txt:
            if len(linha) > 25 and linha[24] == tipo_registro:
                dados = extrair_tipos(
                    linha,
                    layout,
                    campos_data,
                    mapas_auxiliares
                )

               

                registros.append(dados)

    return registros

def formatar_data(valor):
    """Formata os campo que contem data"""
    if valor == '00000000':
        return''
    if valor and len(valor) == 8 and valor.isdigit():
        return f'{valor[0:2]}/{valor[2:4]}/{valor[4:8]}'
    return valor    






