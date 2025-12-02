import streamlit as str
import pandas as pd

str.title("facebook")
str.header("sign in",divider=True)
x = str.text_input("username",max_chars= 15,width="stretch")
y = str.text_input("password",max_chars= 11)
z = str.button("submit")
if z:
    str.write(f"welcome back {x}!")

from sklearn import linear_model
from sklearn.model_selection import train_test_split
df = pd.read_csv("homeprices.csv")
model = linear_model.LinearRegression()
x = df.drop("price",axis="columns")
y = df.drop("area",axis="columns")
model.fit(x,y)
str.write(model.score(x,y) * 100)
xx = str.number_input("what's the area",max_value=7000)
str.write(model.predict([[xx]]))
 #to run use streamlit run "the file" inside the terminal