import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score,precision_score,recall_score
Iris = load_iris()
df = pd.DataFrame(Iris.data, columns=Iris.feature_names)
df['target'] = Iris.target
print(df)
X_train, X_test, y_train, y_test = train_test_split(df[Iris.feature_names],df['target'], test_size=0.3, random_state=20)
rf = RandomForestClassifier(n_estimators=300, random_state=20)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print("Predicted Value:",y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall Score:", recall)
print("F1 Score:", f1)