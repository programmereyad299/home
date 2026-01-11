import joblib
import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Home Price Prediction" , page_icon="🏠")
st.title("Home Price Prediction 🏠")
model = joblib.load('homemodel8.pkl')
st.sidebar.title("Home Details :")

Square_Footage = st.sidebar.slider("Square Footage :" , 503 , 4999 )
Num_Bedrooms = st.sidebar.slider("Number of Bedrooms :" , 1 , 5 )
Num_Bathrooms = st.sidebar.slider("Number of Bathrooms :" , 1 , 3)
Year_Built = st.sidebar.slider("Year Built :" , 1950, 2022 )
Lot_Size = st.sidebar.slider("Lot Size :" , 0.506058219, 4.9893027 )
Garage_Size = st.sidebar.slider("Garage Size :" , 0, 2 )
Neighborhood_Quality = st.sidebar.slider("Neighborhood Quality :" ,1 , 10 )

input_df = pd.DataFrame([[Square_Footage,Num_Bedrooms,Num_Bathrooms,Year_Built,Lot_Size,Garage_Size,Neighborhood_Quality]] , 
                        columns=["Square_Footage","Num_Bedrooms","Num_Bathrooms","Year_Built","Lot_Size","Garage_Size","Neighborhood_Quality"])

btn = st.button("pred")
if btn :
    pred = model.predict(input_df)
    st.success(pred[0])