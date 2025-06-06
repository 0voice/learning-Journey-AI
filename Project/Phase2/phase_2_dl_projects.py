# 🧠 阶段 2：深度学习项目实战代码
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import os

# 1️⃣ 手写数字识别（MNIST 全连接 + CNN）
class SimpleMLP(nn.Module):
    def __init__(self):
        super(SimpleMLP, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        return self.fc2(x)

def train_mnist(model):
    transform = transforms.ToTensor()
    trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(1):
        for imgs, labels in trainloader:
            optimizer.zero_grad()
            output = model(imgs)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 2️⃣ 猫狗图像分类器（使用预训练模型）
def train_dog_cat():
    from torchvision.datasets import ImageFolder
    from torchvision.models import resnet18
    data_dir = "./dogs_cats"
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])
    dataset = ImageFolder(data_dir, transform=transform)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    model = resnet18(pretrained=True)
    model.fc = nn.Linear(model.fc.in_features, 2)
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    criterion = nn.CrossEntropyLoss()
    for imgs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print("猫狗分类训练完成")

# 3️⃣ 面部表情识别（FER2013 + CNN）
def fer2013_cnn():
    # 假设 FER2013 数据集已预处理为 train.csv 格式
    import pandas as pd
    class FERDataset(torch.utils.data.Dataset):
        def __init__(self, csv_file):
            data = pd.read_csv(csv_file)
            self.X = [torch.tensor(list(map(int, row.split())), dtype=torch.float32).reshape(1, 48, 48) / 255.0 for row in data['pixels']]
            self.y = torch.tensor(data['emotion'].values, dtype=torch.long)
        def __len__(self): return len(self.y)
        def __getitem__(self, i): return self.X[i], self.y[i]

    trainset = FERDataset("fer2013_train.csv")
    loader = DataLoader(trainset, batch_size=32, shuffle=True)
    model = SimpleCNN()
    model.conv1 = nn.Conv2d(1, 32, 3, padding=1)  # adjust to grayscale
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    for imgs, labels in loader:
        optimizer.zero_grad()
        output = model(imgs)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
    print("面部表情训练完成")

# 4️⃣ Google Speech Commands语音识别器（使用 torchaudio）
def speech_command_recognizer():
    import torchaudio
    dataset = torchaudio.datasets.SPEECHCOMMANDS("./", download=True)
    print("示例样本:", dataset[0][0].shape, dataset[0][2])  # waveform, sample rate, label

# 5️⃣ 图像风格迁移项目（VGG）
def image_style_transfer():
    from torchvision.models import vgg19
    print("请参考 torch tutorial: https://pytorch.org/tutorials/advanced/neural_style_tutorial.html")

# 主函数
if __name__ == '__main__':
    print("1.MNIST MLP\n2.MNIST CNN\n3.猫狗分类\n4.FER表情识别\n5.语音命令识别\n6.图像风格迁移")
    c = input("选择项目编号: ")
    if c == '1': train_mnist(SimpleMLP())
    elif c == '2': train_mnist(SimpleCNN())
    elif c == '3': train_dog_cat()
    elif c == '4': fer2013_cnn()
    elif c == '5': speech_command_recognizer()
    elif c == '6': image_style_transfer()
