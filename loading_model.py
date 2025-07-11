import streamlit as str
import joblib as jb
str.header("home prices",divider=True)
model = jb.load("homeprices_linearregression.pkl")
x = str.slider("THE AREA OF THE HOUSE?",min_value=1000,max_value=7000)
y = model.predict([[x]])
if str.button("predict the price!"):
    str.write(y)