from house_price_prediction import house_price_prediction
from spam_classifier import spam_classifier
from iris_classification import iris_classification
from kmeans_segmentation import kmeans_customer_segmentation
from credit_risk_model import credit_risk_model

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
