# AI 智能面试官

一个结合语音识别（STT）、自然语言问答与评分的 AI 模拟面试系统。支持语音作答、自动识别并打分反馈。

## 💡 功能说明

- 自动提问（从题库随机抽题）
- 用户语音作答（支持 WAV）
- 语音转文字（STT：Speech-to-Text）
- NLP 评分（语言通顺度、要点覆盖）
- 分数反馈 & 建议

## 🧰 技术组件

- `Whisper` / `SpeechRecognition`：语音转文字
- `HuggingFace Transformers`：问答建模
- `自定义评分函数`：打分与反馈

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

## 运行
```bash
python app.py
```
上传一段语音回答，返回文本及打分：
```json
{
  "question": "Tell me about a time you handled conflict.",
  "transcript": "There was a situation in my last job where...",
  "score": 8.7,
  "feedback": "Well-structured, missing one key detail about resolution."
}
```

