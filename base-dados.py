from rdflib import Graph, URIRef
from urllib.parse import urlparse
import urllib.request 
import requests
import urllib.error
import pandas as pd
from requests import HTTPError, Timeout, ConnectionError, ConnectTimeout, ReadTimeout
import os.path
#from requests import ReadTimeout, ConnectTimeout, InvalidURL
#from pandas import read_excel
#from openpyxl import load_workbook

#caminho para extracao da base de dados xls
PATH = "/home/samara/Documentos/tcc/imagensBD1/"
#caminho para extracao da base de dados rdfm
PATH1 = '/home/samara/Documentos/tcc/imagensBD2/'

def baixarImagens(url, nomeImg, id):
    
    try:
        
        # verifica se há alguma url corrompida
        if("http" not in url):
            url = "http:/"+url
            
        connection = requests.get(url)
        connection.raise_for_status()
        img_data = requests.get(url).content
        with open(nomeImg, 'wb') as handler:
            handler.write(img_data)
    except HTTPError as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("ERRO:", e.response.status_code, e.response.reason)
    except ConnectionError as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("Falha ao estabelecer a conexão.")
    except Timeout as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("ERRO:", e)
    except ConnectTimeout as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("ERRO:", e)
    except ReadTimeout as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("ERRO:", e)

def criarDiretorio(img, caminho, id):
    #arquivo = PATH+id+".jpg"
    arquivo = caminho+id+".jpg"
    
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        if not os.path.exists(arquivo):
            baixarImagens(img, arquivo, id)
    else:
        if not os.path.exists(arquivo):
            baixarImagens(img, arquivo, id)    
    
def extrairInfo(url):
    
    # separa as partes da url
    temp  = urlparse(url)
    label = ""
    
    try:
        # pega a string que contém o nome da característica e splita por '/'
        label = temp.path.split('/')
        # o nome da característica sempre está na última posição do vetor splitado
        label = label[len(label)-1]
    except:
        print("Erro ao extrair label.")
        
    return label

def recuperarDados():
      
    G              = Graph()
    G              = G.parse("dataset.xml", format="xml")
    desaparecidos  = G.subjects()
    
    for pessoa in desaparecidos:
        atributos = G.predicate_objects(pessoa)
        id        = extrairInfo(pessoa)
        for carac, valor in atributos:
            label = extrairInfo(carac)
            #print("O ID é: ", id, "\n")
            #print(label, ": ", valor)
            if(label == "img"):
                #arquivo = PATH+id+".jpg"
                criarDiretorio(valor, PATH1, id)
                #if not os.path.exists(arquivo):
                 #   baixarImagens(valor, arquivo, id)
        #print('------------ X -----------\n')
                
def recuperarDadosxlsx():
    
    arq_excel = "myosotis_database.xlsx" 
    df        = pd.read_excel(arq_excel)
    linhas    = len(df['id'])
    
    for linha in range(linhas):
        id  = str(df['id'][linha])
        img = str(df['imagem'][linha])
        #txt = img
        #conf = "http:"

        if img == 'nan' or "http:" not in img:
            continue   
        criarDiretorio(img, PATH, id)
        #if not os.path.exists(arquivo):
        #   baixarImagens(img, arquivo, id)       
        #print(id, img)
        
def main():
    
    recuperarDados()
    #recuperarDadosxlsx()
    
if __name__ == '__main__':
    main()