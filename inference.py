import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('CropPrediction\cropmodel.pkl', 'rb'))
scaler = pickle.load(open('CropPrediction\scalar.pkl', 'rb'))
class_names = ['apple','blackgram','chickpea','coconut','coffee','cotton','grapes','jute','kidneybeans','lentil','maize','mango','mothbeans','mungbean','muskmelon','orange','papaya','pigeonpeas','pomegranate','rice']

def predict(df):
    df = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    df = scaler.transform(df)
    # numpy_array = df.to_numpy()
    predictions = model.predict(df)-1
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

n = 2195						
p = 107
k = 34
temp = 32	
hum = 66.413269		
ph = 6.780064
rain = 177.774507

df = pd.DataFrame({ 
    'N':[n],
    'P':[p], 
    'K':[k], 
    'temperature':[temp], 
    'humidity':[hum],
    'ph':[ph],
    'rainfall':[rain]

})
print(predict(df))