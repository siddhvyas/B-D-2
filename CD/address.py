import re

class TACGenerator:
    def __init__(self):
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"T{self.temp_count}"

    def precedence(self, op):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

    def infix_to_postfix(self, expr):
        output, stack = [], []
        tokens = re.findall(r'\w+|[+\-*/=()]', expr)
        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(token):
                    output.append(stack.pop())
                stack.append(token)
        return output + stack[::-1]

    def postfix_to_tac(self, postfix, target):
        stack, code = [], []
        for token in postfix:
            if token.isalnum():
                stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                temp = self.new_temp()
                code.append(f"{temp} = {a} {token} {b}")
                stack.append(temp)
        code.append(f"{target} = {stack.pop()}")
        return code

    def generate_tac(self, expr):
        target, rhs = map(str.strip, expr.split('='))
        postfix = self.infix_to_postfix(rhs)
        return self.postfix_to_tac(postfix, target)

# Example usage
if __name__ == "__main__":
    expr = input("Enter an expression: ")
    tac = TACGenerator().generate_tac(expr)
    print("Generated 3-address code:")
    print("\n".join(tac))
