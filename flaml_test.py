from flaml import AutoML
model = AutoML()
import pandas as pd
df = pd.read_csv("homeprices.csv")
x = df.drop(columns="price")
y = df["price"]
model.fit(x,y,task = "regression",time_budget=360,estimator_list=['lgbm', 'rf', 'xgboost'])
print(model.score(x,y))
