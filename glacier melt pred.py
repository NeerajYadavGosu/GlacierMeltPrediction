# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 03:28:34 2023

@author: NEERAJ GOSU
"""
// hi
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image

image = Image.open('C:/Users/NEERAJ GOSU/Desktop/Glacier melt prediction system/snow_mountain.jpeg')

st.image(image, caption='Glacier Melt in Himalayas')
#
# loading the saved models

glacier_model = pickle.load(open('C:/Users/NEERAJ GOSU/Desktop/Glacier melt prediction system/saved models/glacier_model.sav', 'rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('GLACIER MELT Prediction System',
                          
                          ['Glacier melt',
                           ],
                          icons=['snow'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Glacier melt'):
    
    # page title
    st.title('Glacier Melt Prediction\n Enter the inputs:')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        temperature = st.text_input('Temperature in Air:')       
    with col2:
        precipitation = st.text_input('Precipitation avg annual:')
    
    with col3:
        elevation = st.text_input('height of glacier above sealevel:')
    
    with col1:
        slope = st.text_input('steepness of glacier:')
    
    with col2:
        aspect = st.text_input('glacier facing direction(Aspect):')
    
    with col3:
        thickness = st.text_input('Glacier Thickness:')
    
    with col1:
        albedo = st.text_input('Albedo:')
    
    with col2:
        cloudcover = st.text_input('cloud cover on glacier:')
   
    with col3:
        snowcover = st.text_input('snow cover:')
    
    with col1:
        vegetationcover= st.text_input('vegetation cover:')
     
    
    
    
    # code for Prediction
    glacier_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Glacier melt Test Result:'):
        glacier_prediction = glacier_model.predict([[temperature, precipitation,elevation,slope,aspect,thickness,albedo,cloudcover,snowcover,vegetationcover]])
        
        if (glacier_prediction[0] == 1):
          glacier_diagnosis = 'The Glacier is melting'
        else:
          glacier_diagnosis = 'The Glacier is not melting'
        
    st.success(glacier_diagnosis)




