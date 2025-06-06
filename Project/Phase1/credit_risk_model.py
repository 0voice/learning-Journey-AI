import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def credit_risk_model():
    df = pd.read_csv("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv")
    df = df.dropna()
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df = pd.get_dummies(df.select_dtypes(include=[object]), drop_first=True).join(df.select_dtypes(include=[np.number]))
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("💳 信用评分预测")
    print("Accuracy:", accuracy_score(y_test, y_pred))
