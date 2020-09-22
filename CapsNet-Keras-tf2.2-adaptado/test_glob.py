import csv
import cv2
import glob, os
from faces import * 
from preproc import *
import numpy as np
import pandas as pd
import PIL
from PIL import Image

CSV_UFJF = 'UFJF.csv'

def busca_csv(id_img):
    
    df_data = pd.read_csv(CSV_UFJF)
    df_data.set_index('id_imagem', inplace=True) # tornando a coluna id_imagem em indice
    caracteristicas = 'teste'
        
    try:
        #caracteristicas = df_data.loc[id_img].values
        caracteristicas = df_data.loc[id_img]['cor_pele']
        print("MINHA CARACTERISTICA É", caracteristicas)
        return caracteristicas
    except:
        print("Imagem"+str(id_img)+" não encontrada.\n")
        
def load_data(DIRETORIO):
    
    x       = [] # lista das imagens
    y       = [] # lista de atributos das imagens (corCabelo, corOlhos...)
    id_img  = 0
    print(DIRETORIO)
    print("vou pro for")
    for i in glob.glob(DIRETORIO):
        print("cheguei no for")
        img             = Image.open(i)
        img             = img.resize((30, 30), PIL.Image.ANTIALIAS)
        pixels          = np.asarray(img).astype('float32') #transforma a imagem em um array de pixels
        pixels          = pixels/pixels.max()
        id_img          = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
        caracteristicas = busca_csv(id_img)

        x.append(pixels)
        y.append(caracteristicas)

    return x,y

load_data('/home/samara/Documentos/tcc/CONJ_TREINO/*.jpg')