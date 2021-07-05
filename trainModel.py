from sklearn.model_selection import train_test_split
from tensorflow import keras
import pandas as pd
import numpy as np


model = keras.models.load_model('creditDataModel')

data = pd.read_csv('processed_data.csv')
xData = data.iloc[:,:-1]
yData = data.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(xData,yData,test_size=.2)

model.fit(x_train,y_train,epochs=150,batch_size=32,verbose=0)


model.save('trainedModel')