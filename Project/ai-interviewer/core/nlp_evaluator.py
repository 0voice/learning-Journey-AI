from core.scoring import simple_scoring

def evaluate_answer(question, answer_text):
    # 这里可以扩展为 HuggingFace BERT 相似度模型打分
    score, feedback = simple_scoring(question, answer_text)
    return score, feedback
