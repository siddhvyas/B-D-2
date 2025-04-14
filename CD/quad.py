import re

class QuadrupleGenerator:
    def __init__(self):
        self.temp_count = 0

    def generate_temp(self):
        self.temp_count += 1
        return f"T{self.temp_count}"

    def precedence(self, op):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

    def infix_to_postfix(self, expr):
        ops, out = [], []
        for token in re.findall(r'\w+|[+\-*/^=()]', expr):
            if token.isalnum(): out.append(token)
            elif token == '(': ops.append(token)
            elif token == ')':
                while ops[-1] != '(': out.append(ops.pop())
                ops.pop()
            else:
                while ops and self.precedence(ops[-1]) >= self.precedence(token):
                    out.append(ops.pop())
                ops.append(token)
        return out + ops[::-1]

    def postfix_to_quadruples(self, postfix):
        stack, quads = [], []
        for token in postfix:
            if token.isalnum(): stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                result = self.generate_temp()
                quads.append((result, token, a, b))
                stack.append(result)
        return stack[-1], quads

    def generate_quadruples(self, expr):
        target, rhs = map(str.strip, expr.split('='))
        postfix = self.infix_to_postfix(rhs)
        _, quads = self.postfix_to_quadruples(postfix)
        quads.append((target, '=', quads[-1][0], ''))
        return quads


def main():
    expr = input("Enter an expression: ")
    quads = QuadrupleGenerator().generate_quadruples(expr)
    
    # Print Quadruples
    print(f"{'Result':<10}{'Operator':<10}{'Operand1':<10}{'Operand2':<10}")
    print("="*40)
    for quad in quads:
        print(f"{quad[0]:<10}{quad[1]:<10}{quad[2]:<10}{quad[3]:<10}")

if __name__ == "__main__":
    main()
