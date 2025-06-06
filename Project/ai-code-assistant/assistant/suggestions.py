import autopep8

def give_suggestions(code):
    suggestions = []
    if '==' in code and 'None' in code:
        suggestions.append(\"建议使用 'is None' 替代 '== None'\")
    formatted = autopep8.fix_code(code)
    if formatted != code:
        suggestions.append(\"建议格式化代码 (PEP8)\")
    return suggestions
