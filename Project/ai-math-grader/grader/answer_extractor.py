import re

def parse_questions(text):
    """
    示例文本：
    Q1: 2x + 5 = ?
    A1: 3x + 5
    Q2: 1/4 + 1/4 = ?
    A2: 0.5
    """
    questions = {}
    lines = text.split('\\n')
    for i in range(0, len(lines) - 1, 2):
        qid = f\"Q{i//2+1}\"
        match_q = re.search(r'[:：]\\s*(.+)', lines[i])
        match_a = re.search(r'[:：]\\s*(.+)', lines[i+1])
        if match_q and match_a:
            questions[qid] = {
                'expected': match_q.group(1).strip(),
                'actual': match_a.group(1).strip()
            }
    return questions
