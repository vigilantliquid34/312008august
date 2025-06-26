import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv("have_insurance.csv",index_col=None)
print(df)
x = df[["age"]]
y = df[["have_insurance"]]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5,random_state=42)
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred,y_test)
print(model.score(x_test,y_test))
#0.875 accurate