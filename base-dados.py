from rdflib import Graph, URIRef
from urllib.parse import urlparse
import urllib.request
import pandas as pd
from pandas import ExcelFile

PATH = "C:/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/Imagens/"
    
def baixarImagens(url, nomeImg, id):
    
    try:
        urllib.request.urlretrieve(url, nomeImg)
    except:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        
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
                baixarImagens(valor, PATH+id+".jpg", id)
        #print('------------ X -----------\n')
        
def imprimirDadosxlsx():
    arq_excel = "myosotis_database.xlsx"
    
    df = pd.read_excel(arq_excel)
    colunas = df.columns
    
    linha = len(df['id'])
    
    #baixarImagens("http://portal.mj.gov.br/Desaparecidos/Fotos//1236Foto2", PATH+'840.jpeg', 840)
    
    for c1 in range(linha):
        id = str(df['id'][c1])
        img = str(df['imagem'][c1])
        baixarImagens(img+".jpg", PATH+id+".jpg", id)
        #print(id, img)        
        
def main():
    
    recuperarDados()
    imprimirDadosxlsx()
    
if __name__ == '__main__':
    main()