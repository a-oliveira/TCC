import csv
#import cv2
import glob, os
#from faces import *
import numpy as np
import pandas as pd
from PIL import Image

CSV_UFJF    = 'UFJF2.csv'
IMGS_UFJF   = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/ProjetoImagensUFJF/'
CONJ_TREINO = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/CONJ_TREINO/*.jpg'

def nome(diretorio):

    nome = diretorio.split("\\") # pega apenas o 'id.jpg'
    nome = nome[1]
    nome = nome.split(".jpg")  # segundo split para pegar apenas o id
    return nome[0]

'''
def nome(diretorio):

    #nome = diretorio.split('imagensBD2/') # pega apenas o 'id.jpg'
    nome = diretorio.rsplit('/', 1) # pega apenas o 'id.jpg'
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
                try:
                    cv2.imwrite(salvaFotoCortada, imagem)
                except:
                    continue
#salvaImagem()