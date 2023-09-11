import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create a pandas dataframe from the given data
data = pd.read_csv("C:/Users/hp/OneDrive/Desktop/machine learning/Decision_Tree_ Dataset.csv")
print(data.head())
# split the data into training and testing sets
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train, X_test, y_train, y_test)
# build a decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
from sklearn import tree
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(25,20)) 

feature_names = [1,2,3,4,sum]
class_names = ['yes', 'no']

_ = tree.plot_tree(model,feature_names= feature_names,class_names= class_names,filled=True)

plt.show()
# make predictions on the testing set and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)