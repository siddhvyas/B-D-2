import re

memory = {'int': 4, 'float': 4, 'double': 8, 'char': 1, 'bool': 1, 'long': 8, 'short': 2}

def analyze_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    decls = re.findall(r'\b(int|float|double|char|bool|long|short)\s*(\w+)(?:\s*=\s*[^;]*)?\s*[;,]', code) 
    vars = [{'name': v, 'type': t, 'used': False} for t, v in decls]

    # Remove declarations to avoid false 'used' positives
    code_wo_decls = re.sub(r'\b(int|float|double|char|bool|long|short)\s+\w+(?:\s*=\s*[^;]*)?\s*[;,]', '', code)
    for var in vars:
        if re.search(r'\b' + re.escape(var['name']) + r'\b', code_wo_decls):
            var['used'] = True

    print(f"{'ID':<5}{'Variable':<12}{'Type':<10}{'Used':<6}{'Defined':<9}{'Memory'}")
    print("=" * 50)
    for i, var in enumerate(vars, 1):
        print(f"{i:<5}{var['name']:<12}{var['type']:<10}{int(var['used']):<6}{'1':<9}{memory.get(var['type'], '?')}")

# Example usage
code = input("Enter file path: ")
analyze_code(code)
