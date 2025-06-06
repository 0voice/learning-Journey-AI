from chinese_sentiment import chinese_sentiment_analysis
from news_classification import news_classification
from faq_qa import faq_qa_system
from translate import translate_zh_en
from chatbot import simple_chatbot

if __name__ == '__main__':
    print("1. 中文情感分析\n2. 新闻文本分类\n3. FAQ问答系统\n4. 中英翻译\n5. ChatBot 聊天机器人")
    choice = input("选择项目编号：")
    if choice == '1': chinese_sentiment_analysis()
    elif choice == '2': news_classification()
    elif choice == '3': faq_qa_system()
    elif choice == '4': translate_zh_en()
    elif choice == '5': simple_chatbot()
