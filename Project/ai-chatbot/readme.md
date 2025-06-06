# AI 聊天机器人 🤖

这是一个基于 GPT2 中文模型构建的简易聊天机器人，支持 API 形式调用。

## ✅ 功能简介
- 支持中文输入与自然语言对话
- 使用 Transformers + Flask 构建服务接口
- 轻量模型，支持本地推理部署

## 📦 安装依赖
```bash
pip install -r requirements.txt
```

## 🚀 启动服务
```bash
python app.py
```
默认监听地址为：http://127.0.0.1:5000/chat

## 📡 请求示例（POST）
```json
{
  "query": "你能介绍一下机器学习吗？"
}
```

## 📁 项目结构说明
```
ai-chatbot/
├── app.py                  # Flask 接口入口
├── requirements.txt        # 所需依赖
├── models/
│   └── load_model.py       # 加载模型与分词器
├── utils/
│   └── prompt_builder.py   # 构造对话提示词
└── README.md               # 项目说明文档
```

## 🔗 模型来源
使用开源模型：[uer/gpt2-chinese-cluecorpussmall](https://huggingface.co/uer/gpt2-chinese-cluecorpussmall)

"""
