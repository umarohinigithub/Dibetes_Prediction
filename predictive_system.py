# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#from tensorflow import keras

import pickle
##loading the saved model
loaded_model=pickle.load(open('C:/Users/UMA/Machine Learnings/Diabetics_machine _learning project/trained_model.pick','rb'))#reading the binary


input_data=(148,72,35,33.6,.627,50)
##changing the input data to numpy array
input_data_as_numpy_aaray=np.asarray(input_data)
#reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_aaray.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
    print('The person is not diabetic')
else:
    print('The person is diabetic')