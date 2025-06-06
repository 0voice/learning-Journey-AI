# AI 编程助手

一个轻量级 AI Copilot 助手，结合代码生成、语法检查与智能提示，支持常见编程语言（Python、JS 等）。

## 🔧 功能模块

- 🚀 代码生成（支持自然语言 prompt → Python/JS 代码）
- 🧪 错误检测（基于 AST/语法解析）
- 💡 Copilot 式补全建议（支持片段优化）

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

## 🚀 启动方式
```bash
python app.py
```

## 🔁 示例
提交 prompt：
```json
{ "prompt": "写一个函数判断字符串是否回文" }
```
返回代码 + 语法报告：

```json
{
  "code": "def is_palindrome(s): return s == s[::-1]",
  "lint": "No syntax errors found.",
  "suggestions": ["考虑添加输入类型检查"]
}
```

## 🗂 模块说明
- assistant/code_generator.py：LLM 接入模块（如 ChatGPT API 或本地模型）

- assistant/syntax_checker.py：AST 语法校验与错误行提示

- assistant/suggestions.py：代码优化建议（格式、命名、健壮性）
