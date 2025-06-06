# 文本模型目录

此目录用于存放文本特征提取相关模型，例如：

- 预训练的 BERT、RoBERTa、DistilBERT 等 Transformer 模型
- 微调好的文本分类或嵌入模型
- 模型权重文件（pytorch .bin 等）
- 模型加载脚本（可选）

示例：

- `pytorch_model.bin`
- `config.json`
- `tokenizer_config.json`

使用示例：

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('./models/text_model')
model = AutoModel.from_pretrained('./models/text_model')
