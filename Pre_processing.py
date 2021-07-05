
import pandas as pd

data = pd.read_csv('credit_data.csv')
#data = data[['income','age','loan','LTI','default']]


data.to_csv('processed_data.csv',index=False,columns=['income','age','loan','LTI','default'])