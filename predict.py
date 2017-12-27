#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:05:19 2017

@author: kais
"""
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential  
from keras.layers.core import Dense, Activation  
from keras.preprocessing import sequence
import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.layers import LSTM
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
file_path= '/media/kais/Kais/datasetRNN/RFM/'
file_name= 'dataset_seq.csv'

file_path_categ= '/home/kais/Projet recherche/shopperRNN/'
file_name_categ= 'outcat.csv'

# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset
dataframe = pandas.read_csv( file_path+file_name ,engine= "python" , skipfooter=3)
dataset = dataframe.values

Y= dataset[:,52:]
#cas RFM 
VecteurY=Y[:,3]
#cas R ou F ou M seulement 
#VecteurY=Y[:,0]
#VecteurY=Y[:,1]
#VecteurY=Y[:,2]
liste_categories=[]
for i in  [1,2,3,4]:
    for j in  [1,2,3,4]:
        for k in [1,2,3,4]:
            s=100*i+10*j+k
            liste_categories.append(s)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(liste_categories)
encoded_Y = encoder.transform(VecteurY)
VecteurY_encoded = np_utils.to_categorical(encoded_Y)

# split into train and test sets
train_size = int(len(dataset) * 0.67) #0.67
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#chaque 3 colonnes correspondent à un time step
nb_colonnesX=52-3
nb_ti=17-1

trainX=dataset[0:train_size,1:nb_colonnesX]
testX=dataset[train_size:len(dataset),1:nb_colonnesX]
trainY= VecteurY_encoded[0:train_size,:]
testY=VecteurY_encoded[train_size:len(dataset),:]       

                  
X_train = numpy.reshape(trainX, (len(trainX), nb_ti,3 ))
X_test = numpy.reshape(testX, (len(testX), nb_ti,3 ))

print trainY.shape[1]
batch_size=30
nb_epoch=2
'''

model = Sequential()
model.add(LSTM(60, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(trainY.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_train, trainY , nb_epoch=3, batch_size=batch_size)
# evaluate the model
scores = model.evaluate(X_test, testY , verbose=1)
print("Accuracy: %.2f%%" % (scores[1]*100))

preds = model.predict(X_train[0:100,:], batch_size=batch_size)

'''

print X_train.shape[1]
print  X_train.shape[2]
def baseline_model():
	# create model
     model = Sequential()
     model.add(LSTM(200, input_shape=(X_train.shape[1], X_train.shape[2])))
     model.add(Dense(trainY.shape[1], activation='softmax'))
     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
     return model
estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=nb_epoch, batch_size=batch_size, verbose=1)
estimator.fit(X_train, trainY)

predictions = estimator.predict(X_test)
print(predictions)
my_pred=encoder.inverse_transform(predictions)
print(my_pred)
my_real_y=VecteurY[train_size:len(dataset)]
print my_real_y #vecteur Y correspondant aux classes de la test set

print  my_pred==my_real_y
m=numpy.array(my_pred==my_real_y)
l=list(m)
print "erreur " + str((float(l.count(False))/len(my_pred))*100)
