# 💬 NLP 实战项目集合（BERT / GPT / 翻译 / ChatBot）

本项目涵盖 5 个经典自然语言处理实战任务，基于 `transformers`, `torch`, `sentence-transformers` 等主流工具构建，适合 NLP 入门
---

## 📂 项目结构
- chinese_sentiment.py--中文情感分析（电商评论）
- news_classification.py--新闻文本分类（THUCNews）
- faq_qa.py--FAQ 问答系统（Embedding 相似度匹配）
- translate.py--中英翻译（Helsinki NMT）
- chatbot.py--简易中文聊天机器人（GPT2）
- main.py--主程序入口（菜单选择）

---

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

## 🚀 启动项目
运行主程序后，按菜单编号选择任务模块：

```bash
python main.py
```

**可选模块：**

- 1 中文情感分析

- 2 新闻文本分类

- 3 FAQ 问答系统

- 4 中英翻译

- 5 简易聊天机器人

## 📌 模型说明
| 模块         | 使用模型名称                                      |
| ---------- | ------------------------------------------- |
| 情感分析       | uer/roberta-base-finetuned-dianping-chinese |
| 新闻分类       | IDEA-CCNL/Erlangshen-Roberta-330M-Chinese   |
| FAQ 问答匹配   | shibing624/text2vec-base-chinese            |
| 中英翻译       | Helsinki-NLP/opus-mt-zh-en                  |
| 中文 ChatBot | uer/gpt2-chinese-cluecorpussmall            |

## 🧠 推荐学习路径
- 熟悉 HuggingFace Transformers 基本使用

- 掌握文本分类 / 生成 / 翻译等主流任务结构

- 学习如何接入 Embedding 模型做问答匹配

- 理解 Prompt + 解码策略在 ChatBot 生成中的作用

## 📚 参考资料
- [HuggingFace Transformers](https://huggingface.co/transformers/)

- [Sentence Transformers](https://www.sbert.net/)

- [THUCNews 数据集](https://thunlp.oss-cn-qingdao.aliyuncs.com/THUCNews.zip)
