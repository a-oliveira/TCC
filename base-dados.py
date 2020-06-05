from rdflib import Graph, URIRef
from urllib.parse import urlparse
import urllib.request
import urllib.error
import pandas as pd

PATH = "C:/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensMyosotis/"
#PATH = "C:/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/Imagens UFJF/"
    
def baixarImagens(url, nomeImg, id):
    
    try:
        urllib.request.urlretrieve(url, nomeImg)
    except urllib.error.ContentTooShortError as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("URL Erro:", e.reason)
    except urllib.error.HTTPError as e:
        print("Erro ao salvar a imagem do desaparecido id: ", id)
        print("HTTP ERRO", e.code, ":", e.reason)
        
        
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
                
def recuperarDadosxlsx():
    
    arq_excel = "myosotis_database.xlsx" 
    df        = pd.read_excel(arq_excel)
    colunas   = df.columns
    linhas    = len(df['id'])
    
    
    for linha in range(linhas):
        id  = str(df['id'][linha])
        img = str(df['imagem'][linha])
        if img == 'nan':
            continue
        baixarImagens(img, PATH+id+".jpg", id)
        #print(id, img)      
        
        
        
def main():
    
    #recuperarDados()
    recuperarDadosxlsx()
    
if __name__ == '__main__':
    main()