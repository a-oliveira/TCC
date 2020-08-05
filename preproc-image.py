import PIL 
import csv
import glob, os
from numpy import *
from PIL import Image
from matplotlib import pyplot
from resizeimage import resizeimage
from keras.preprocessing.image import *
import pandas as pd

BASE_MYOSOTIS = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensMyosotis/*.jpg'
PATH          = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/rotulacao-bd.csv'
LARGURA       = 80
ALTURA        = 80

listaImagens = []
listaY       = []

def nome(diretorio):
    # pega apenas o id.jpg
    nome = diretorio.split("\\")
    nome = nome[1]
    # segundo split para pegar apenas o id
    nome = nome.split(".jpg")
    return nome[0]

def imageToarray():
    
    for i in glob.glob(BASE_MYOSOTIS):
        img    = Image.open(i)
        img    = img.resize((LARGURA, ALTURA), PIL.Image.ANTIALIAS)
        pixels = asarray(img).astype('float32')
        pixels = pixels/pixels.max()
        # transforma id da imagem em inteiro antes de passar pra busca
        busca_csv(int(nome(i)))
        #print(nome(i))
        #pyplot.imshow(pixels)
        listaImagens.append(pixels)
    return listaImagens

def busca_csv(id_img):
    df_data = pd.read_csv(PATH)
    #tornando a coluna id_imagem em indice
    df_data.set_index('id_imagem', inplace=True)
    print(df_data.loc[id_img].values)
    
busca_csv(47)
#lista = imageToarray()