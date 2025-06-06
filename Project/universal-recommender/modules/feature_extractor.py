import torch
from transformers import AutoTokenizer, AutoModel
from PIL import Image
import base64
import io

# 加载文本模型
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
text_model = AutoModel.from_pretrained('bert-base-uncased')

# 加载图像模型（示例：ResNet）
import torchvision.models as models
import torchvision.transforms as transforms
image_model = models.resnet50(pretrained=True)
image_model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
])

def extract_text_features(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = text_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach()

def extract_image_features(image_base64):
    if image_base64 is None:
        return None
    image_bytes = base64.b64decode(image_base64)
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img_t = transform(image).unsqueeze(0)
    with torch.no_grad():
        features = image_model(img_t)
    return features

def extract_features(text, image_base64):
    text_feat = extract_text_features(text)
    img_feat = extract_image_features(image_base64)
    if img_feat is None:
        return text_feat
    return torch.cat([text_feat, img_feat], dim=1)
