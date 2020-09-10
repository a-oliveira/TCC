import csv
#import cv2
import glob, os
#from faces import *
import numpy as np
import pandas as pd
from PIL import Image


CSV_UFJF    = 'UFJF.csv'
IMGS_UFJF   = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensUFJF/'
CONJ_TREINO = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/CapsNet-Keras-tf2.2/CONJ_TREINO/*.jpg'

def nome(diretorio):

    nome = diretorio.split("\\") # pega apenas o 'id.jpg'
    nome = nome[1]
    nome = nome.split(".jpg")  # segundo split para pegar apenas o id
    return nome[0]

'''
def nome(diretorio):

    #nome = diretorio.split('imagensBD2/') # pega apenas o 'id.jpg'
    nome = diretorio.rsplit('/', 1) # pega apenas o 'id.jpg'
    print(nome)
    nome = nome[1]
    nome = nome.split(".jpg")  # segundo split para pegar apenas o id
    
    return nome[0]
'''
               
def salvaImagem():
    imagem = None
    with open(CSV_UFJF, 'r') as rotulacao:
        leitor = csv.DictReader(rotulacao, delimiter=',')
        
        for coluna in leitor:
            caminhoFoto = IMGS_UFJF+str(coluna['id_imagem'])+".jpg"            
            if os.path.exists(IMGS_UFJF):
                if not os.path.exists(CONJ_TREINO):
                    os.makedirs(CONJ_TREINO) #cria diretório pra salvar a imagem lá
                    
                salvaFotoCortada = CONJ_TREINO+str(coluna['id_imagem'])+".jpg"
                imagem           = cropFaces(caminhoFoto)
                cv2.imwrite(salvaFotoCortada, imagem)
                
def busca_csv(id_img):
    
    df_data = pd.read_csv(CSV_UFJF)
    df_data.set_index('id_imagem', inplace=True) # tornando a coluna id_imagem em indice
        
    try:
        #caracteristicas = df_data.loc[id_img].values
        caracteristicas = df_data.loc[id_img]['cor_pele']
        return caracteristicas
    except:
        print("Imagem"+str(id_img)+" não encontrada.\n")
        
def load_data(DIRETORIO):
    
    x       = [] # lista das imagens
    y       = [] # lista de atributos das imagens (corCabelo, corOlhos...)
    id_img  = 0
    
    for i in glob.glob(DIRETORIO):
        
        try:
            img             = Image.open(i)
            img             = img.resize((30, 30), PIL.Image.ANTIALIAS)
            pixels          = np.asarray(img).astype('float32') #transforma a imagem em um array de pixels
            pixels          = pixels/pixels.max()
            id_img          = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
            caracteristicas = busca_csv(id_img)
            x.append(pixels)
            y.append(caracteristicas)
        except:
            continue

    return np.array(x), np.array(y)
     
#salvaImagem()