from tensorflow import keras
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
model = keras.models.load_model('creditDataModel')

data = pd.read_csv('processed_data.csv')
xData = data.iloc[:,:-1]
yData = data.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(xData,yData,test_size=.2)
loss, acc = model.evaluate(x_test,y_test,verbose=0)
print('Test Accuracy: %.3f' % acc)