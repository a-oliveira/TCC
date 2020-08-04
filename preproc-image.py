import PIL 
import csv
import glob, os
from numpy import *
from PIL import Image
from matplotlib import pyplot
from resizeimage import resizeimage
from keras.preprocessing.image import *

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
            print(linha[1:6])

#lista = imageToarray()

target()