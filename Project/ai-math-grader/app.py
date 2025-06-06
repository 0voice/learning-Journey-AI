from flask import Flask, request, jsonify
from grader.ocr_reader import extract_text
from grader.answer_extractor import parse_questions
from grader.logic_checker import compare_answers
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/grade', methods=['POST'])
def grade():
    file = request.files['image']
    img_array = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    text = extract_text(img_array)

    parsed = parse_questions(text)
    results = {qid: compare_answers(ans['expected'], ans['actual']) | {'expected': ans['expected'], 'actual': ans['actual']}
               for qid, ans in parsed.items()}

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
