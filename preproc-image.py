import PIL 
import glob, os
from numpy import *
from PIL import Image
from matplotlib import pyplot
from resizeimage import resizeimage
from keras.preprocessing.image import *

BASE_MYOSOTIS = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensMyosotis/*.jpg'
PASTA_BKP     = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/teste/'
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
        
lista = imageToarray()    