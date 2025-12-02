import streamlit as str
import time

str.header("app.py")
str.write("hehe")
str.badge("home",color="green")
str.write(":ship:")

button1 = str.button("click my buns")
button2 = str.button("click my ass")

if button1:
    str.write("you clicked my buns!")
elif button2:
    str.write("you clicked my ass!") 
       
x = str.slider("pick a number and i will mulyiply it by 2",1,100)  

def multiplication(x):
    return x*2

y = multiplication(x)
   
str.write(y) 
########################################################
 #to run use streamlit run "the file" inside the terminal