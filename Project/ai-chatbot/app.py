from flask import Flask, request, jsonify
from models.load_model import load_chat_model
from utils.prompt_builder import build_prompt
import torch

app = Flask(__name__)
tokenizer, model = load_chat_model()

def chat_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("助手：")[-1].strip()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    prompt = build_prompt(query)
    answer = chat_response(prompt)
    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(debug=True)
