# 🤖 阶段 1：机器学习项目示例代码

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ 房价预测模型（线性回归）
def house_price_prediction():
    df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
    X = df.drop("medv", axis=1)
    y = df["medv"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R2 Score:", r2_score(y_test, y_pred))

# 2️⃣ 垃圾邮件分类器（逻辑回归 / SVM / Naive Bayes）
def spam_classifier():
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.preprocessing import LabelEncoder

    df = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv", sep='\t', header=None, names=['label', 'message'])
    X = df['message']
    y = LabelEncoder().fit_transform(df['label'])
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# 3️⃣ 鸢尾花分类（sklearn 经典数据集）
def iris_classification():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Iris Classification Accuracy:", accuracy_score(y_test, y_pred))

# 4️⃣ KMeans 客户分群分析（营销）
def kmeans_customer_segmentation():
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mall_customers.csv")
    kmeans = KMeans(n_clusters=4, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df[['Annual Income (k$)', 'Spending Score (1-100)']])
    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='Set1')
    plt.title("Customer Segmentation")
    plt.show()

# 5️⃣ 信用评分风险预测模型
def credit_risk_model():
    df = pd.read_csv("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv")
    df = df.dropna()
    df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})
    df = pd.get_dummies(df.select_dtypes(include=[object]), drop_first=True).join(df.select_dtypes(include=[np.number]))
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Credit Churn Accuracy:", accuracy_score(y_test, y_pred))

# 主函数：交互式运行
if __name__ == "__main__":
    print("选择运行的项目:")
    print("1. 房价预测")
    print("2. 垃圾邮件分类")
    print("3. 鸢尾花分类")
    print("4. 客户分群分析")
    print("5. 信用评分预测")
    option = input("输入数字选择: ")
    if option == '1':
        house_price_prediction()
    elif option == '2':
        spam_classifier()
    elif option == '3':
        iris_classification()
    elif option == '4':
        kmeans_customer_segmentation()
    elif option == '5':
        credit_risk_model()
