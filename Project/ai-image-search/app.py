from flask import Flask, request, jsonify
from utils.feature_extractor import extract_features
from utils.index_builder import load_faiss_index, search_index
import cv2
import os

app = Flask(__name__)
INDEX_PATH = 'index/faiss_index.bin'
IMAGE_DB = 'static/images'

# 加载索引和特征提取器
index, id_map = load_faiss_index(INDEX_PATH)
print(f"[INFO] Loaded index with {len(id_map)} images.")

@app.route('/search', methods=['POST'])
def search_image():
    file = request.files['image']
    img_array = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    query_vec = extract_features(img_array)

    results = search_index(index, query_vec, id_map, top_k=5)

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
