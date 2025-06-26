from sklearn import linear_model
import pandas as pd
print("all good")
df = pd.read_csv("homeprices.csv")
from sklearn.model_selection import train_test_split
model = linear_model.LinearRegression()
x = df[["area"]]
y = df[["price"]]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=42)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred,y_test)
print(model.score(x_test,y_test))
#0.9232979137811631 accurate yayyyy