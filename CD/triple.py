import re

class TripleGenerator:
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

    def postfix_to_triples(self, postfix):
        stack, triples = [], []
        for token in postfix:
            if token.isalnum(): stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                triples.append((token, a, b))
                stack.append(f"T{len(triples)}")
        return stack[-1], triples

    def generate_triples(self, expr):
        target, rhs = map(str.strip, expr.split('='))
        postfix = self.infix_to_postfix(rhs)
        _, triples = self.postfix_to_triples(postfix)
        triples.append(('=', triples[-1][2], '', target))
        return triples


def main():
    expr = input("Enter an expression: ")
    triples = TripleGenerator().generate_triples(expr)
    
    # Print Triples
    print(f"{'Operator':<10}{'Operand1':<10}{'Operand2':<10}")
    print("="*30)
    for triple in triples:
        print(f"{triple[0]:<10}{triple[1]:<10}{triple[2]:<10}")

if __name__ == "__main__":
    main()
