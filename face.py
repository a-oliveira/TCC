import csv
import cv2
import glob, os
import sys
import numpy as np

IMGS_UFJF = os.path.join('data', 'ImagensUFJF/')
CONJ_TREINO = os.path.join('data', 'CONJ_TREINO/')
CSV_UFJF = os.path.join(IMGS_UFJF, 'UFJF.csv')

def cropFaces(diretorio):
    #listaFaces = []
    
    cascPath = "haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(diretorio)
    #print(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.imread(image, 1)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    #print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        image = image[y:y+h, x:x+w]

    #listaFaces.append(image)
    #detected_faces = np.array(listaFaces)
    
    return image

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

salvaImagem()

#print(cropFaces('data/crop_tes/155.jpg'))
'''
cv2.imshow('tela',nam)
cv2.waitKey(0)'''