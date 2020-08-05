import PIL 
import csv
import glob, os
from numpy import *
from PIL import Image
from matplotlib import pyplot
from resizeimage import resizeimage
from keras.preprocessing.image import *
import pandas as pd

PATH = '/home/samara/Downloads/base_ufjf.csv'
BASE_MYOSOTIS = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensMyosotis/*.jpg'
PATH          = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/rotulacao-bd.csv'
LARGURA       = 80
ALTURA        = 80

listaImagens = []

def nome(diretorio):
    nome = diretorio.split("\\")
    nome = nome[1]
    return nome

def imageToarray():
    
    j = 0
    for i in glob.glob(BASE_MYOSOTIS):
        img    = Image.open(i)
        img    = img.resize((LARGURA, ALTURA), PIL.Image.ANTIALIAS)
        pixels = asarray(img).astype('float32')
        pixels = pixels/pixels.max()
        #pyplot.imshow(pixels)
        listaImagens.append(pixels)
    return listaImagens
        
def target():
    
    with open(PATH, newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha[:6])

#lista = imageToarray()

target()



def busca_csv(id_img):
    df_data = pd.read_csv(arquivo)
    #tornando a coluna id_imagem em indice
    df_data.set_index('id_imagem', inplace=True)
    print(df_data.loc[id_img])

busca_csv(40)
