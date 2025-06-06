# AI 数学作业批改助手

一个结合 OCR、NLP 和规则判断的自动批改工具。支持读取手写/打印数学题与答案，并判断其正确性。

## ✨ 功能特色

- OCR：识别数学题与学生答案（支持手写）
- NLP：提取题干、答案，处理表达式
- 逻辑判断：与标准答案比对，支持等价判断（如 0.5 vs 1/2）

## 📦 依赖安装

```bash
pip install -r requirements.txt
```

**⚠️ 注意：如果使用 Tesseract OCR，需先安装 Tesseract：**
- [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

## 启动
```bash
python app.py
```

## 示例使用：
上传 examples/test1.jpg，输出 JSON 批改结果:
```json
{
  "Q1": {"expected": "3x+5", "actual": "3x + 5", "correct": true},
  "Q2": {"expected": "1/2", "actual": "0.5", "correct": true}
}
```



