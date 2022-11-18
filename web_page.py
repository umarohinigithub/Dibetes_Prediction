# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:45:44 2022

@author: UMA
"""
import numpy as np
import pickle
import streamlit as st

###loading the saved model
loaded_model=pickle.load(open('C:/Users/UMA/Machine Learnings/Diabetics_machine _learning project/trained_model.pick','rb'))#reading the binary

#creating a function for prediction
def pred_diabetic(input_data):
    
    
    ##changing the input data to numpy array
    input_data_as_numpy_aaray=np.asarray(input_data)
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_aaray.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
      return 'The person is not diabetic'
    else:
     return 'The person is diabetic'
 
def main():

   ##giving a title
   st.title('Web App for Diabetic prediction')
   
   
   #getting the input data from user
   
   Age=st.text_input('Age')
   SkinThickness=st.text_input('Skin Thickness value')
   Glucose =st.text_input('Glucose Level')
   BMI=st.text_input('BMI Value')
   BloodPressure=st.text_input('Bloodpressure level')
   Diabeticpedigreefunction=st.text_input('Diabetic Pedigree value')


    ##code for prediction
   diagnosis = '' 
   
   #creating a button for prediction
   
   if st.button('Diabetes Test Result'):
       diagnosis = pred_diabetic([Age,SkinThickness,Glucose,BMI,BloodPressure,Diabeticpedigreefunction])

   st.success(diagnosis)
  
if __name__=='__main__':
    main()

    