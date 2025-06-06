import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from mnist.models import SimpleCNN
from .fer_dataset import FERDataset

def train_fer():
    dataset = FERDataset("fer2013_train.csv")
    loader = DataLoader(dataset, batch_size=32, shuffle=True)
    model = SimpleCNN()
    model.conv1 = nn.Conv2d(1, 32, 3, padding=1)  # Adjust for grayscale
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    for imgs, labels in loader:
        optimizer.zero_grad()
        output = model(imgs)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
    print("😊😠😭 表情识别完成")
