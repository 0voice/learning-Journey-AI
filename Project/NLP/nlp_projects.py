# 💬 阶段 4：NLP 实战项目代码（BERT/GPT 方向）

# 1️⃣ 中文情感分析器（电商评论 + BERT）
def chinese_sentiment_analysis():
    print("✅ 使用 BERT + Transformers 实现中文情感分析：")
    print("1. 安装依赖：transformers, datasets, torch")
    print("2. 示例模型：uer/roberta-base-finetuned-dianping-chinese")
    print("3. 推理示例代码：")
    print("""
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-dianping-chinese")
print(classifier("这款手机性价比很高，值得购买！"))
    """)

# 2️⃣ 新闻文本分类器（THUCNews）
def news_classification():
    print("✅ 使用 THUCNews 语料 + BERT 微调进行分类")
    print("1. 数据集链接：https://thunlp.oss-cn-qingdao.aliyuncs.com/THUCNews.zip")
    print("2. 示例模型：IDEA-CCNL/Erlangshen-Roberta-330M-Chinese")
    print("3. 微调建议使用 transformers Trainer + datasets.load_dataset")

# 3️⃣ FAQ 问答系统（Embedding 相似度匹配）
def faq_qa_system():
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('shibing624/text2vec-base-chinese')
    faq = ["如何联系客服？", "如何退货？", "如何修改密码？"]
    faq_emb = model.encode(faq, convert_to_tensor=True)
    query = "怎么联系客服啊"
    q_emb = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(q_emb, faq_emb)
    best_idx = scores.argmax()
    print(f"匹配到问题: {faq[best_idx]}")

# 4️⃣ 翻译模型微调（Helsinki NMT）
def translate_zh_en():
    from transformers import MarianMTModel, MarianTokenizer
    src_text = ["我爱自然语言处理"]
    model_name = 'Helsinki-NLP/opus-mt-zh-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    inputs = tokenizer(src_text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    print("翻译结果:", tokenizer.batch_decode(translated, skip_special_tokens=True))

# 5️⃣ 简易 ChatBot（Transformers + Prompt）
def simple_chatbot():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model_name = "uer/gpt2-chinese-cluecorpussmall"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    while True:
        query = input("你说: ")
        if query.lower() in ['exit', 'quit']:
            break
        inputs = tokenizer.encode(query, return_tensors='pt')
        outputs = model.generate(inputs, max_length=50, pad_token_id=tokenizer.eos_token_id)
        print("机器人:", tokenizer.decode(outputs[0], skip_special_tokens=True))

# 主菜单
if __name__ == '__main__':
    print("1. 中文情感分析\n2. 新闻文本分类\n3. FAQ问答系统\n4. 中英翻译\n5. ChatBot 聊天机器人")
    choice = input("选择项目编号：")
    if choice == '1': chinese_sentiment_analysis()
    elif choice == '2': news_classification()
    elif choice == '3': faq_qa_system()
    elif choice == '4': translate_zh_en()
    elif choice == '5': simple_chatbot()
