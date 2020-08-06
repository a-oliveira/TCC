import PIL 
import csv
import glob, os
from numpy import *
from PIL import Image
from matplotlib import pyplot
from resizeimage import resizeimage
from keras.preprocessing.image import *
import pandas as pd

BASE_UFJF     = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensUFJF/*.jpg'
PATH_BKP      = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensTreino'
PATH          = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/rotulacao-bd.csv'
IMG_EXISTE    = False

LARGURA       = 80
ALTURA        = 80

listaImagens = []
listaY       = []

'''
#print(nome(i))
#pyplot.imshow(pixels) - serve para printar a imagem em forma de gráfico
'''

def nome(diretorio):
    # pega apenas o id.jpg
    nome = diretorio.split("\\")
    nome = nome[1]
    # segundo split para pegar apenas o id
    nome = nome.split(".jpg")
    return nome[0]

def criarDiretorio(id_img, imagem):
    foto = PATH_BKP+"\\"+str(id_img)+".jpg"
    
    if not os.path.exists(PATH_BKP):
        os.makedirs(PATH_BKP)
        imagem.save(foto)
    else:
        if not os.path.exists(foto):
            imagem.save(foto)
            
def busca_csv(id_img, objImg):
    
    df_data = pd.read_csv(PATH)
    df_data.set_index('id_imagem', inplace=True) # tornando a coluna id_imagem em indice
    
    try:
        caracteristicas = df_data.loc[id_img].values
        criarDiretorio(id_img, objImg) # armazena a imagem encontrada no csv
        IMG_EXISTE = True
        return caracteristicas
    except:
        print("Imagem"+str(id_img)+" não encontrada.\n")
    
    return False
            
def load_data():
    
    x = [] # lista das imagens
    y = [] # lista de atributos das imagens (corCabelo, corOlhos...)
    
    for i in glob.glob(BASE_UFJF):
        img    = Image.open(i)
        img    = img.resize((LARGURA, ALTURA), PIL.Image.ANTIALIAS)
        i      = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
        caracteristicas = busca_csv(i, img)
        
        if(IMG_EXISTE):
            pixels = asarray(img).astype('float32') #transforma a imagem em um array de pixels
            pixels = pixels/pixels.max()
            x.append(pixels)
            y.append(caracteristicas)
        else:
            continue
        
    return x,y
    
x,y = load_data()

print(x)