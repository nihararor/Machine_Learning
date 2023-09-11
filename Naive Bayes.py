from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score,precision_score,recall_score,confusion_matrix
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=20)
print(X_train, X_test, y_train, y_test)
gaussiannb = GaussianNB()
gaussiannb.fit(X_train, y_train)
y_pred = gaussiannb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print("Accuracy in percentage:", accuracy*100)
print("Precision in percentage:", precision*100)
print("Recall Score in percentage:", recall*100)
print("F1 Score in percentage:", f1*100)
cm=confusion_matrix(y_test, y_pred)
print(cm)