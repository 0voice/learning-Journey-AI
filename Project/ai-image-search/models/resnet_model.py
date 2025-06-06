# 如果需要将模型封装成类可使用此模块
from torchvision import models
import torch.nn as nn

class ResNetEmbedder(nn.Module):
    def __init__(self):
        super().__init__()
        base = models.resnet50(pretrained=True)
        self.model = nn.Sequential(*list(base.children())[:-1])

    def forward(self, x):
        return self.model(x).squeeze()
