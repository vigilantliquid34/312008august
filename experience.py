import streamlit as str
import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv("experience - Sheet1.csv")
str.title("predictions")
model = LinearRegression()
x = df.drop(columns="salary")
y = df[["salary"]]
model.fit(x,y)



a_experience = str.slider("what is the experience?",min_value=0,max_value=15)
a_testscore = str.slider("what was the test score?",min_value=0,max_value=10)
a_interviewscore = str.slider("what was the interview score?",min_value=0,max_value=10)
x_pred = [[a_experience,a_testscore,a_interviewscore]]
str.write(model.predict(x_pred))
mod_score =model.score(x,y)
str.text(f"i'm {mod_score * 100} sure!")

import matplotlib.pyplot as plt
str.checkbox("ass")