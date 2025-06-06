from modules.embedding_index import FaissIndex

# 假设已构建好全量索引
global_index = None

def build_index(all_features, all_ids):
    global global_index
    dim = all_features.shape[1]
    global_index = FaissIndex(dim)
    global_index.add_items(all_features, all_ids)

def get_recommendations(query_features, top_k=5):
    if global_index is None:
        return []
    results = global_index.search(query_features, k=top_k)
    return results[0] if results else []
