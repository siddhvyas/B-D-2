# \bswitch – matches the word switch with a word boundary

# \s* – allows for optional spaces

# .*? – matches the contents of the parentheses (non-greedy way to handle parameters)

# \s* – optional spaces

# \{ – matches the opening curly brace
import re

def check_if_else_and_switch_statements(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Updated regular expressions
        if_else_found = re.search(r'\b(if|else if|else)\b', content)
        switch_found = re.search(r'\bswitch\s*\(.*?\)\s*\{', content)

        if if_else_found and switch_found:
            return "The file contains both 'if-else' statements and a 'switch' statement."
        elif if_else_found:
            return "The file contains 'if-else' statements."
        elif switch_found:
            return "The file contains a 'switch' statement."
        else:
            return "The file contains neither 'if-else' nor 'switch' statements."

    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

filename = input("Enter the path to the text file: ")
result = check_if_else_and_switch_statements(filename)
print(result)
