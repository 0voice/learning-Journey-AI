from flask import Flask, request, jsonify
from core.question_bank import get_random_question
from core.stt_engine import transcribe_audio
from core.nlp_evaluator import evaluate_answer

app = Flask(__name__)

@app.route('/interview', methods=['POST'])
def interview():
    audio = request.files['audio']
    filepath = 'temp.wav'
    audio.save(filepath)

    question = get_random_question()
    transcript = transcribe_audio(filepath)
    score, feedback = evaluate_answer(question, transcript)

    return jsonify({
        'question': question,
        'transcript': transcript,
        'score': round(score, 2),
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
