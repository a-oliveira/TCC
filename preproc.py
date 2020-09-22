import csv
import glob
import os
import numpy as np
import pandas as pd
from PIL import Image
from face import cropFaces

IMGS_UFJF = os.path.join('data', 'ImagensUFJF')
CONJ_TREINO = os.path.join('data', 'CONJ_TREINO')
CSV_UFJF = os.path.join(IMGS_UFJF, 'UFJF.csv')


def pega_id(img_name, sistema):

    if sistema == 'linux':
        nome = img_name.rsplit('/', 1)
    else:
        img_name = img_name.split("\\")[-1]

    nome = img_name.split(".jpg")  # segundo split para pegar apenas o id

    return nome[0]


def salvaImagem():
    imagem = None
    with open(CSV_UFJF, 'r') as rotulacao:
        leitor = csv.DictReader(rotulacao, delimiter=',')

        for coluna in leitor:
            caminhoFoto = IMGS_UFJF+str(coluna['id_imagem'])+".jpg"
            if os.path.exists(IMGS_UFJF):
                if not os.path.exists(CONJ_TREINO):
                    # cria diretório pra salvar a imagem lá
                    os.makedirs(CONJ_TREINO)

                salvaFotoCortada = CONJ_TREINO+str(coluna['id_imagem'])+".jpg"
                imagem = cropFaces(caminhoFoto)
                try:
                    cv2.imwrite(salvaFotoCortada, imagem)
                except:
                    continue


'''
if __name__ == '__main__':
'''
