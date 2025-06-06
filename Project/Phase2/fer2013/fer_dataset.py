import torch
import pandas as pd

class FERDataset(torch.utils.data.Dataset):
    def __init__(self, csv_file):
        data = pd.read_csv(csv_file)
        self.X = [torch.tensor(list(map(int, row.split())), dtype=torch.float32).reshape(1, 48, 48)/255.0 for row in data['pixels']]
        self.y = torch.tensor(data['emotion'].values, dtype=torch.long)
    def __len__(self): return len(self.y)
    def __getitem__(self, i): return self.X[i], self.y[i]
