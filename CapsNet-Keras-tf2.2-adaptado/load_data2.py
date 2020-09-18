import glob
import pandas as pd
import numpy as np
from preproc import *
import PIL
from PIL import Image
#import cv2

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
        pass
        #print("Imagem {} não encontrada.".format(+str(id_img)))
        
def load_data(DIRETORIO):

    x       = [] # lista das imagens
    j       = 0
    id_img  = 0
    y       = [[0,0,0,0,0]] # lista de atributos das imagens (corCabelo, corOlhos...)
    
    for o in range(0,914):
        y.append([0,0,0,0,0]) 

    for i in glob.glob(DIRETORIO):
        
        id_img = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
        
        try:
            img             = Image.open(i)
            img             = img.resize((30, 30), PIL.Image.ANTIALIAS)
            pixels          = np.asarray(img).astype('float32') #transforma a imagem em um array de pixels
            pixels          = pixels/pixels.max()
            #id_img          = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
            x.append(pixels)
                        
            corPele = busca_csv(id_img)
            
            if corPele == 2:
                y[j][0] = 1#id_img
                
            elif corPele == 3:
                y[j][1] = 1#id_img
                
            elif corPele == 4:
                y[j][2] = 1#id_img
                
            elif corPele == 5:
                y[j][3] = 1#id_img
                
            elif corPele == 6:
                y[j][4] = 1#id_img
            j += 1
        except:
            #print("Erro ao abrir a imagem {}.".format(nome(i)))
            pass #continue
    
    y = np.array(y)
    x = np.array(x)

    return x,y

'''x, y = load_data('/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/CONJ_TREINO/*.jpg')
print("Eu sou o shape do x: {} \nEu sou o shape do y: {}".format(x.shape,y.shape))
print(y[0][0])
print(y[1])
print(y[80])'''
