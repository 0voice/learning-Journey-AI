import torch
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np
import cv2

model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])  # 去除最后分类层
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

def extract_features(image):
    with torch.no_grad():
        input_tensor = transform(image).unsqueeze(0)
        features = model(input_tensor)
        return features.squeeze().numpy()
