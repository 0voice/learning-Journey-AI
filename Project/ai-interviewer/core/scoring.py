from difflib import SequenceMatcher

def simple_scoring(q, a):
    """
    基于关键词覆盖 + 结构长度简易打分（可替换为深度模型）
    """
    score = 5.0
    if len(a.split()) > 20:
        score += 2
    if any(keyword in a.lower() for keyword in ["challenge", "resolved", "team", "conflict"]):
        score += 2
    if "don't know" in a.lower():
        score -= 3
    feedback = "Good structure." if score >= 7 else "Try elaborating more with examples."
    return min(score, 10), feedback
