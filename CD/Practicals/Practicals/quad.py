# Quadruple Code Generator
import re

class QuadrupleGenerator:
    def __init__(self):
        self.temp = 0

    def new_temp(self):
        self.temp += 1
        return f"T{self.temp}"

    def prec(self, op):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

    def infix_to_postfix(self, expr):
        out, stack = [], []
        for tok in re.findall(r'\w+|[+\-*/=()]', expr):
            if tok.isalnum():
                out.append(tok)
            elif tok == '(':
                stack.append(tok)
            elif tok == ')':
                while stack and stack[-1] != '(':
                    out.append(stack.pop())
                stack.pop()
            else:
                while stack and self.prec(stack[-1]) >= self.prec(tok):
                    out.append(stack.pop())
                stack.append(tok)
        while stack:
            out.append(stack.pop())
        return out

    def generate_quadruples(self, expr):
        lhs, rhs = map(str.strip, expr.split("="))
        stk, quads = [], []
        for tok in self.infix_to_postfix(rhs):
            if tok.isalnum():
                stk.append(tok)
            else:
                b, a = stk.pop(), stk.pop()
                t = self.new_temp()
                quads.append((t, tok, a, b))
                stk.append(t)
        quads.append((lhs, '=', stk.pop(), ''))
        return quads

if __name__ == "__main__":
    expr = input("Enter an expression (e.g., z = (a + b) * c): ")
    gen = QuadrupleGenerator()
    quads = gen.generate_quadruples(expr)

    print(f"{'Result':<10}{'Operator':<10}{'Operand1':<10}{'Operand2':<10}")
    print("=" * 40)
    for q in quads:
        print(f"{q[0]:<10}{q[1]:<10}{q[2]:<10}{q[3]:<10}")
