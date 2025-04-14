import re

def checkloop(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        
        for_match = re.search(r'\bfor\s+.+\s+in\s+.+:', content)
        while_match = re.search(r'\bwhile\s+.+:', content)
        do_match = re.search(r'\bdo\s*\{.*?\}\s*while\s*\(.*?\)\s*;', content, re.DOTALL)

        if for_match:
            return 'This file contain for loop statment'
        elif while_match:
            return 'This file contain while loop statement'
        elif do_match:
            return 'This file contain do while loop statement'
        else:
            return 'This file does not contain any loop statement'
        
    except FileNotFoundError:
        return f'This file {filename} does not exist'
    
filename = input("Enter file name: ")
result = checkloop(filename)
print(result)