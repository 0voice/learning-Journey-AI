# 图像模型目录

此目录用于存放图像特征提取相关模型，例如：

- 预训练的 ResNet、EfficientNet、Vision Transformer 等
- 微调后的图像分类或特征提取模型
- 模型权重文件（.pth 或 .pt 格式）
- 模型加载代码（可选）

示例：

- `resnet50.pth`
- `model_config.json`

使用示例：

```python
import torch
import torchvision.models as models

model = models.resnet50()
model.load_state_dict(torch.load('./models/image_model/resnet50.pth'))
model.eval()
