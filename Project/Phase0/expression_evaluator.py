def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output, stack = [], []
    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    output.extend(reversed(stack))
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(eval(f"{a}{token}{b}"))
    return stack[0]

def expression_evaluator():
    expr = input("Enter infix expression (space-separated): ")
    postfix = infix_to_postfix(expr)
    print("Postfix:", postfix)
    print("Result:", evaluate_postfix(postfix))
