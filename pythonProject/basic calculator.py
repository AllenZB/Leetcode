def evaluate_expr(stack):
    res = stack.pop() if stack else 0
    while stack and stack[-1] != ')':
        sign = stack.pop()
        if sign == '+':
            res += stack.pop()
        else:
            res -= stack.pop()
    return res

def calculate(s: str) -> int:
    stack = []
    n, operand = 0, 0
    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch.isdigit():
            operand = (10 ** n * int(ch)) + operand
            n += 1
        elif ch != " ":
            if n:
                stack.append(operand)
                n, operand = 0, 0
        if ch == '(':
            res = evaluate_expr(stack)
            stack.pop()
            stack.append(res)
        else:
            stack.append(ch)
    if n:
        stack.append(operand)
    return evaluate_expr(stack)
s="(1+(4+5+2)-3)+(6+8)"
print(calculate(s))