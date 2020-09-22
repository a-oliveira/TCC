import PIL 
import csv
import glob, os
from numpy import *
from PIL import Image
from matplotlib import pyplot
from resizeimage import resizeimage
from keras.preprocessing.image import *
import pandas as pd

# '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensTreino/*.jpg'
PATH          = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/rotulacao-bd.csv'
PATH_BKP      = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensTreino'
BASE_UFJF     = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/ImagensUFJF/*.jpg'
CONJ_TREINO   = '/Users/Pandessa/Documents/MEGA/UFRRJ/TCC/Projeto/CONJ_TREINO/*.jpg'
CONJ_TESTE    = '/Users/Pandessa/Documents/MEGA/UFRJ/TCC/Projeto/CONJ_TESTE/*.jpg'

'''
PATH          = '/home/samara/Downloads/rotulacao-bd.csv'
PATH_BKP      = '/home/samara/Documentos/tcc/imagens_treino/'
BASE_UFJF     = '/home/samara/Documentos/tcc/imagensBD2/*.jpg'
CONJ_TREINO   = '/home/samara/Documentos/tcc/imagens_treino/*.jpg'
'''

LARGURA       = 80
ALTURA        = 80

'''
#print(nome(i))
#pyplot.imshow(pixels) - serve para printar a imagem em forma de gráfico
'''

def nome(diretorio):

    nome = diretorio.split("\\") # pega apenas o 'id.jpg'
    nome = nome[1]
    nome = nome.split(".jpg")  # segundo split para pegar apenas o id
    return nome[0]

'''
def nome(diretorio):

    #nome = diretorio.split('imagensBD2/') # pega apenas o 'id.jpg'
    nome = diretorio.split('imagens_treino/') # pega apenas o 'id.jpg'
    nome = nome[1]
    nome = nome.split(".jpg")  # segundo split para pegar apenas o id
    
    return nome[0]
'''
def criarDiretorio(id_img, imagem):
    foto = PATH_BKP+"//"+str(id_img)+".jpg" #salvar no windows
    #foto = PATH_BKP+"/"+str(id_img)+".jpg" #salvar no ubuntu
    
    if not os.path.exists(PATH_BKP):
        os.makedirs(PATH_BKP)
        try:
            imagem.save(foto)
        except:
            print("Erro ao salvar a imagem "+str(id_img)+".")
    else:
        if not os.path.exists(foto):
            try:
                imagem.save(foto)
            except:
                print("Erro ao salvar a imagem "+str(id_img)+".")
            
def busca_csv(id_img, objImg):
    
    df_data = pd.read_csv(PATH)
    df_data.set_index('id_imagem', inplace=True) # tornando a coluna id_imagem em indice
        
    try:
        caracteristicas = df_data.loc[id_img].values
        return caracteristicas
    except:
        print("Imagem"+str(id_img)+" não encontrada.\n")
            
def salva_imagem():
    
    id_img  = 0
    df_data = pd.read_csv(PATH)
    df_data.set_index('id_imagem', inplace=True) # tornando a coluna id_imagem em indice
    
    for i in glob.glob(BASE_UFJF):
        
        try:
            img = Image.open(i)
        except:
            print("Imagem "+nome(i)+" não pode ser aberta.")
            
        id_img = int(nome(i)) # transforma id da imagem em inteiro antes de criar o diretorio
        
        try:
            df_data.loc[id_img].values # se a imagem tá na planilha de rotulação, ela é salva na pasta
            img = img.resize((LARGURA, ALTURA), PIL.Image.ANTIALIAS)
            criarDiretorio(id_img, img) # armazena a imagem encontrada no csv
        except:
            continue
        
def load_data(DIRETORIO):
    
    x       = [] # lista das imagens
    y       = [] # lista de atributos das imagens (corCabelo, corOlhos...)
    id_img  = 0
    
    for i in glob.glob(DIRETORIO):
        
        img             = Image.open(i)
        pixels          = asarray(img).astype('float32') #transforma a imagem em um array de pixels
        pixels          = pixels/pixels.max()
        id_img          = int(nome(i)) # transforma id da imagem em inteiro antes de passar pra busca
        caracteristicas = busca_csv(id_img, img)
        x.append(pixels)
        y.append(caracteristicas)
        
    return x,y

#salva_imagem()
#x_treino,y_treino = load_data(CONJ_TREINO)
#x_teste,y_teste   = load_data(CONJ_TESTE)

#data = (x_treino, y_treino), (x_teste,y_teste)

#print(data)
#print(y_treino[0])
#pyplot.imshow(x_treino[0])