import torchvision
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
from torchvision import transforms
from .models import SimpleMLP

def train_mnist_mlp():
    transform = transforms.ToTensor()
    trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    loader = DataLoader(trainset, batch_size=64, shuffle=True)
    model = SimpleMLP()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(1):
        for imgs, labels in loader:
            optimizer.zero_grad()
            output = model(imgs)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
        print(f"[MLP] Epoch {epoch+1}, Loss: {loss.item():.4f}")
