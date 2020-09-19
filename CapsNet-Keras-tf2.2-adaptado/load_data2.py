import glob
import pandas as pd
import numpy as np
from preproc import *
import PIL
from PIL import Image
from keras.utils import to_categorical
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
    id_img  = 0
    y       = [] # lista de atributos das imagens (corCabelo, corOlhos...)
    cor_pele = ["parda", "branca", "preta", "amarela", "indigena"]
    mapping = {}

    for k in range(len(cor_pele)):
    	mapping[cor_pele[k]] = k

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
            pass #continue
    
    y = np.array(y)
    x = np.array(x)
    #y = to_categorical(y.astype('float32'))

    return x, to_categorical(y)
'''
x, y = load_data('/home/samara/Documentos/tcc/CONJ_TREINO/*.jpg')
print("Eu sou o shape do x: {} \nEu sou o shape do y: {}".format(x.shape,y.shape))

print(to_categorical(y))


print(y[0][0])
print(y[1])
print(y[80])'''
