import PIL
from PIL import Image
from keras.preprocessing.image import *
from resizeimage import resizeimage
import numpy as np
import glob, os

BASE_MYOSOTIS = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensMyosotis/*.jpg'
PASTA_BKP     = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/teste/'

def nome(diretorio):
    nome = diretorio.split("\\")
    nome = nome[1]
    return nome

def load_imagens():
    
    largura = 200
    altura  = 200
    
    for i in glob.glob(BASE_MYOSOTIS):
        img = Image.open(i)
        img = img.resize((largura, altura), PIL.Image.ANTIALIAS)
        img.save(PASTA_BKP+nome(i))
        #print(nome(i))

print(load_imagens())
