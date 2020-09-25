import os
import glob
import pandas as pd
import numpy as np
from preproc import pega_id
import PIL
from PIL import Image
from keras.utils import to_categorical
#import cv2


def busca_csv(id_img, arquivo):

    df_data = pd.read_csv(arquivo)
    # tornando a coluna id_imagem em indice
    df_data.set_index('id_imagem', inplace=True)

    try:
        #caracteristicas = df_data.loc[id_img].values
        caracteristicas = df_data.loc[id_img]['cor_pele']
        return caracteristicas
    except:
        pass
        #print("Imagem {} não encontrada.".format(+str(id_img)))


def load_data(diretorio, arquivo, sistema):
    image_path = os.path.join(diretorio, '*.jpg')
    print("opening {} images".format(image_path))

    x = []  # lista das imagens
    id_img = 0
    y = []  # lista de atributos das imagens (corCabelo, corOlhos...)
    cor_pele = ["parda", "branca", "preta", "amarela", "indigena"]
    num_classes = len(cor_pele)
    mapping = {}

    for k in range(len(cor_pele)):
        mapping[cor_pele[k]] = k

    for i in glob.glob(image_path):

        # transforma id da imagem em inteiro antes de passar pra busca
        id_img = int(pega_id(i, sistema))

        try:
            img = Image.open(i)
            img = img.resize((30, 30), PIL.Image.ANTIALIAS)
            pixels = np.array(img)
            if np.shape(pixels) == (30, 30, 3):

                corPele = busca_csv(id_img, arquivo)

                if corPele > 1 and corPele < 7:
                    x.append(pixels)

                if corPele == 2:
                    y.append(mapping['branca'])

                elif corPele == 3:
                    y.append(mapping['preta'])

                elif corPele == 4:
                    y.append(mapping['parda'])

                elif corPele == 5:
                    y.append(mapping['amarela'])

                elif corPele == 6:
                    y.append(mapping['indigena'])

        except:
            #print("Erro ao abrir a imagem {}.".format(nome(i)))
            pass  # continue

    x = np.array(x)
    x = x/x.max()
    y = np.array(y)

    return x, to_categorical(y, num_classes)

def decoder(y):
    if y == 0:
        x = 'não tem marca ou tatuagem'
    elif y == 1:
        x = 'tem marca ou tatuagem'
    elif y == 2:
        x = 'branca'
    elif y == 3:
        x = 'preta'
    elif y == 4:
        x = 'parda'
    elif y == 5:
        x = 'amarela'
    elif y == 6:
        x = 'indígena'
    elif y == 7:
        x = 'preto'
    elif y == 8:
        x = 'branco'
    elif y == 9:
        x = 'loiro'
    elif y == 10:
        x = 'colorido'
    elif y == 11:
        x = 'azul'
    elif y == 12:
        x = 'castanho'
    elif y == 13:
        x = 'preto'
    elif y == 14:
        x = 'verde'
    elif y == 15:
        x = 'feminino'
    elif y == 16:
        x = 'masculino'
    elif y == 17:
        x = 'grisalho'
    else:
        return 'Não existe'
    
    return x

'''
if __name__ == '__main__':

    X, y = [], []
    arquivos = ['UFJF.csv', 'MYOSOTIS.csv']
    diretorios = ['data\\ImagensUFJF\\', 'data\\ImagensMyosotis\\']

    for diretorio, arquivo in zip(diretorios, arquivos):
        data, labels = load_data(diretorio, arquivo)
        X.extend(data)
        y.extend(labels)

    X = np.array(X)
    y = np.array(y)
    print("Eu sou o shape do x: {} \nEu sou o shape do y: {}".format(X.shape,y.shape))
'''
