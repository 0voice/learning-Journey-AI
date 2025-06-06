from flask import Flask, request, jsonify
from modules.feature_extractor import extract_features
from modules.recommender import get_recommendations

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    text_input = data.get('text', '')
    image_data = data.get('image', None)  # 期望 base64 编码字符串

    features = extract_features(text_input, image_data)
    recommendations = get_recommendations(features)

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
