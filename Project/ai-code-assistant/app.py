from flask import Flask, request, jsonify
from assistant.code_generator import generate_code
from assistant.syntax_checker import check_syntax
from assistant.suggestions import give_suggestions

app = Flask(__name__)

@app.route('/code', methods=['POST'])
def code_assistant():
    data = request.json
    prompt = data.get('prompt', '')
    code = generate_code(prompt)
    lint_result = check_syntax(code)
    suggestions = give_suggestions(code)

    return jsonify({
        'code': code,
        'lint': lint_result,
        'suggestions': suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
