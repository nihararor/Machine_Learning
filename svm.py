from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
import pandas as pd
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.6, random_state=52)
print(X_train,X_test, y_train, y_test)
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
precision = precision_score(y_test, y_pred, average='weighted')
print('Precision:', precision)
recall = recall_score(y_test, y_pred, average='weighted')
print('Recall:', recall)
f1 = f1_score(y_test, y_pred, average='weighted')
print('F1 Score:', f1)