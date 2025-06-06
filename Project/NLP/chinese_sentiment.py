def chinese_sentiment_analysis():
    print("\u2705 使用 BERT + Transformers 实现中文情感分析：")
    print("1. 安装依赖：transformers, datasets, torch")
    print("2. 示例模型：uer/roberta-base-finetuned-dianping-chinese")
    print("3. 推理示例代码：")
    print("""
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-dianping-chinese")
print(classifier("这款手机性价比很高，值得购买！"))
    """)
