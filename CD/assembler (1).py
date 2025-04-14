def create_mnemonic_table(mnemonic_data):
    print("Mnemonic Table:")
    print("{:<10} {:<40}".format("Mnemonic", "Description"))
    print("-" * 50)
    
    for line in mnemonic_data:
        parts = line.split(",")
        if len(parts) == 2:
            mnemonic = parts[0].strip()
            description = parts[1].strip()
            print("{:<10} {:<40}".format(mnemonic, description))

def create_symbol_table(symbol_data):
    print("\nSymbol Table:")
    print("{:<10} {:<10}".format("Variable", "Value"))
    print("-" * 20)
    
    symbols = {}
    for line in symbol_data:
        parts = line.split(",")
        if len(parts) == 2:
            variable = parts[0].strip()
            value = int(parts[1].strip())
            symbols[variable] = value
            print("{:<10} {:<10}".format(variable, value))

    return symbols

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    mnemonic_data = []
    symbol_data = []

    # Parse the content of the file
    current_section = None
    
    for line in content:
        line = line.strip()
        if line.startswith("#"):
            current_section = line[1:].strip()  # Get section name without '#'
        elif line:  # If it's not an empty line
            if current_section == "Mnemonics":
                mnemonic_data.append(line)
            elif current_section == "Symbols":
                symbol_data.append(line)

    return mnemonic_data, symbol_data

def perform_addition(symbols):
    # Simulate loading values from symbols A and B
    reg_a = symbols['A']
    reg_b = symbols['B']
    
    # Perform addition
    result = reg_a + reg_b
    
    # Store result in RESULT variable
    symbols['RESULT'] = result
    
    return result

def main():
    filename = "data.txt"  # Specify your file name here
    mnemonic_data, symbol_data = read_file(filename)
    
    create_mnemonic_table(mnemonic_data)
    symbols = create_symbol_table(symbol_data)

    # Perform addition of A and B
    result = perform_addition(symbols)
    
    print(f"\nThe sum of A and B is: {result}")
    print(f"Stored in RESULT: {symbols['RESULT']}")

if __name__ == "__main__":
    main()
