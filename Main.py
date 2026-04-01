import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv("Telco-Customer-Churn.csv")

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

df = df.drop('customerID', axis=1) 
df = pd.get_dummies(df, drop_first=True)

X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = LogisticRegression(max_iter=1500)
model.fit(X_train, y_train)

preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)
print("Model Accuracy:", accuracy)

df['Churn'].value_counts().plot(kind='bar')
plt.title("Churn Distribution")
plt.show()

print(df.corr()['Churn'].sort_values(ascending=False).head(10))