#!/usr/bin/env python
# coding: utf-8

# In[150]:


from keras import Sequential
from keras import layers
from keras.layers import Conv2D
import numpy as np

x = layers.Input(shape=[28,28,256], dtype='float32')


# In[151]:


camada1 = Conv2D(filters=256, kernel_size=9, strides=1, padding='valid', activation='relu', name='conv1')(x)

model = Sequential()
model.add(camada1)

model.load_weights('trained_model-11-19.h5', by_name = True)


# In[4]:


from keras.applications.vgg16 import VGG16
model = VGG16()
model.summary()


# In[4]:


# example of using a pre-trained model as a classifier
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
# load an image from file
image = load_img('cat.jpg', target_size=(224, 224))
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
# load the model
model = VGG16()
# predict the probability across all output classes
yhat = model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(yhat)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))

