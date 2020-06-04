from rdflib import Graph, URIRef
from urllib.parse import urlparse
import urllib.request

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
        
        
        
def main():
    
    recuperarDados()
    
if __name__ == '__main__':
    main()