import ast

def check_syntax(code):
    try:
        ast.parse(code)
        return \"No syntax errors found.\"
    except SyntaxError as e:
        return f\"SyntaxError: {e.msg} at line {e.lineno}\"
