import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('cropmodel.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
class_names = ['apple','banana','blackgram','chickpea','coconut','coffee','cotton','grapes','jute','kidneybeans','lentil','maize','mango','mothbeans','mungbean','muskmelon','orange','papaya','pigeonpeas','pomegranate','rice','watermelon']

def predict(df):
    df = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    df = scaler.transform(df)
    predictions = model.predict(df)-1
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

