import glob
import pandas as pd
import numpy as np
from preproc import *
from PIL import Image

CSV_UFJF    = 'UFJF2.csv'
#IMGS_UFJF   = '/home/samara/Documentos/tcc/ImagensUFJF/'
#CONJ_TREINO = '/home/samara/Documentos/tcc/CONJ_TREINO/*.jpg'

def busca_csv(id_img):
    
    df_data = pd.read_csv(CSV_UFJF)
    df_data.set_index('id_imagem', inplace=True) # tornando a coluna id_imagem em indice
        
    try:
        #caracteristicas = df_data.loc[id_img].values
        caracteristicas = df_data.loc[id_img]['cor_pele']
        return caracteristicas
    except:
        print("Imagem {} não encontrada.".format(+str(id_img)))
        
def load_data(DIRETORIO):

    x       = [] # lista das imagens
    y       = [] # lista de atributos das imagens (corCabelo, corOlhos...)
    id_img  = 0
    
    for i in glob.glob(DIRETORIO):
        
        try:
            img             = Image.open(i)
            img             = img.resize((30, 30), PIL.Image.ANTIALIAS)
            pixels          = np.asarray(img).astype('float32')#.reshape(30,30) #transforma a imagem em um array de pixels
            pixels          = pixels/pixels.max()
            id_img          = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
            caracteristicas = busca_csv(id_img)
            x.append(pixels)
            y.append(caracteristicas)
        except:
            print("Erro ao abrir a imagem {}.".format(int(nome(i))))
    
    y = np.array(y)
    x = np.array(x)


    #print('x:',len(x))
    #print('y:',len(y))

    return x,y

#x, y = load_data('/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/CONJ_TREINO/*.jpg')
#print("Eu sou o shape do x: {} \nEu sou o shape do y: {}".format(x.shape[1:],y.shape))