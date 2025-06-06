import faiss
import numpy as np

class FaissIndex:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.items = []

    def add_items(self, features, item_ids):
        np_feats = features.cpu().numpy().astype('float32')
        self.index.add(np_feats)
        self.items.extend(item_ids)

    def search(self, query_feat, k=5):
        np_query = query_feat.cpu().numpy().astype('float32')
        distances, indices = self.index.search(np_query, k)
        results = []
        for dist_list, idx_list in zip(distances, indices):
            res = []
            for dist, idx in zip(dist_list, idx_list):
                if idx < len(self.items):
                    res.append({'id': self.items[idx], 'distance': float(dist)})
            results.append(res)
        return results
