# Three Address Code Generator (TAC)
import re

class TACGENRATE:
    def __init__(self):
        self.temp = 0

    def new_temp(self):
        self.temp += 1
        return f"T{self.temp}"

    def prec(self, op):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

    def inflix_to_postfix(self, expr):
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

    def generate_tac(self, expr):
        lhs, rhs = map(str.strip, expr.split("="))
        stk, tac = [], []
        for tok in self.inflix_to_postfix(rhs):
            if tok.isalnum():
                stk.append(tok)
            else:
                b, a = stk.pop(), stk.pop()
                t = self.new_temp()
                tac.append(f"{t} = {a} {tok} {b}")
                stk.append(t)
        tac.append(f"{lhs} = {stk.pop()}")
        return tac

if __name__ == "__main__":
    print("\n".join(TACGENRATE().generate_tac(input("Enter an expression (e.g., z = (a + b) * c): "))))
