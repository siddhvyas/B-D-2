optab = {
    "MOV": 0x10, "ADD": 0x20, "SUB": 0x30, "JMP": 0x40, "HLT": 0x60,
    "OUT": 0x70, "STO": 0x80, "DS": 0x90, "START": -1, "INP": 0x14
}

symtab, instructions = {}, []
loc = 1000

def parse_instruction(line):
    global loc
    parts = line.split()
    if not parts or parts[0] not in optab: 
        if parts: print(f"Error: invalid mnemonic '{parts[0]}'")
        return

    mnem, op = parts[0], parts[1] if len(parts) > 1 else ""
    if mnem == "START" and op.isdigit():
        loc = int(op); return
    if op and mnem not in ["DS", "START"]:
        symtab.setdefault(op, loc + 1)

    instructions.append((mnem, op))
    print(f"loc {loc} : {mnem} {op} -> 0x{optab[mnem]:X}")
    loc += 4

def main():
    print("Enter assembly code (type 'HLT' to finish):")
    while (line := input().strip()) != "HLT":
        parse_instruction(line)

    print("\nSymbol TABLE:\n")
    print("\n".join(f"{s}\t{a}" for s, a in symtab.items()) or "No symbol")

    print("\nOpcode TABLE:\n")
    for op in optab:
        args = [symtab.get(arg, "No operands") for m, arg in instructions if m == op]
        print(f"{op}\t{', '.join(map(str, args)) if args else ' '}")

if __name__ == "__main__":
    main()
