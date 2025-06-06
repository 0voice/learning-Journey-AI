import torch
import torch.nn as nn

class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        def conv_block(in_c, out_c):
            return nn.Sequential(
                nn.Conv2d(in_c, out_c, 3, padding=1),
                nn.ReLU(),
                nn.Conv2d(out_c, out_c, 3, padding=1),
                nn.ReLU()
            )
        self.enc1 = conv_block(1, 64)
        self.pool = nn.MaxPool2d(2)
        self.dec1 = nn.ConvTranspose2d(64, 1, 2, stride=2)
        self.final = nn.Conv2d(1, 1, 1)

    def forward(self, x):
        x1 = self.enc1(x)
        x2 = self.pool(x1)
        x3 = self.dec1(x2)
        return torch.sigmoid(self.final(x3))

def unet_demo():
    model = UNet()
    dummy_input = torch.rand(1, 1, 128, 128)
    output = model(dummy_input)
    print("U-Net 输出尺寸:", output.shape)
