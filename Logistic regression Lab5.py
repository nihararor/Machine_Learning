import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Iris.csv")
print(df.head())

X = df.drop("Species", axis = 1)
print(X)
y = df["Species"]
print(y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y) 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
a=LogisticRegression(max_iter=1000)
a.fit(X_train, y_train)
print("Accuracy :", a.score(X_test, y_test))

predictions = a.predict(X_test)

residuals = y_test - predictions

plt.scatter(range(len(residuals)), residuals)
plt.show()