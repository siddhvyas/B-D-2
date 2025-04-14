import re

class TripleGenerator:
    def __init__(self):
        self.temp = 0

    def precedence(self, op):
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
                while stack and self.precedence(stack[-1]) >= self.precedence(tok):
                    out.append(stack.pop())
                stack.append(tok)
        while stack:
            out.append(stack.pop())
        return out

    def generate_triples(self, expr):
        lhs, rhs = map(str.strip, expr.split('='))
        stk, triples = [], []
        for tok in self.infix_to_postfix(rhs):
            if tok.isalnum():
                stk.append(tok)
            else:
                b = stk.pop()
                a = stk.pop()
                triples.append((tok, a, b))
                stk.append(f'T{len(triples)}')
        triples.append(('=', triples[-1][2], '', lhs))
        return triples

if __name__ == '__main__':
    expr = input("Enter an expression: ")
    gen = TripleGenerator()
    triples = gen.generate_triples(expr)

    print(f"{'Operator':<10}{'Operand1':<10}{'Operand2':<10}")
    print("=" * 30)
    for t in triples:
        print(f"{t[0]:<10}{t[1]:<10}{t[2]:<10}")
