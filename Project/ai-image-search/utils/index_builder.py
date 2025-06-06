import faiss
import numpy as np
import os
import pickle

def build_index(feature_list, id_map, dim=2048):
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(feature_list).astype('float32'))
    return index

def save_index(index, path, id_map):
    faiss.write_index(index, path)
    with open(path + '.map', 'wb') as f:
        pickle.dump(id_map, f)

def load_faiss_index(index_path):
    index = faiss.read_index(index_path)
    with open(index_path + '.map', 'rb') as f:
        id_map = pickle.load(f)
    return index, id_map

def search_index(index, query_vec, id_map, top_k=5):
    D, I = index.search(np.array([query_vec]).astype('float32'), top_k)
    return [id_map[i] for i in I[0]]
