import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("diabetes.csv")
print(data.head())
x = data['Age'].tolist() 
y = data['BMI'].tolist()
result = sm.OLS(y,x).fit()
print(result.summary())
y_pred = result.predict(x)
plt.scatter(x,y, color = 'r')
plt.scatter(x,y_pred, color= 'g')
plt.plot(x,y_pred, color = 'b')
plt.show()

