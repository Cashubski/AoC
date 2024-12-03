import re

def read_input(filename="input3.txt"):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return ""

def find_valid_multiplications(text):
    # Pattern for instructions:
    # - Multiplication pattern
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    # - Control patterns
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Find all instructions with their positions
    instructions = []
    
    # Find multiplications
    for match in re.finditer(mul_pattern, text):
        x, y = map(int, match.groups())
        instructions.append(('mul', match.start(), x * y))
    
    # Find do() instructions
    for match in re.finditer(do_pattern, text):
        instructions.append(('do', match.start(), None))
    
    # Find don't() instructions
    for match in re.finditer(dont_pattern, text):
        instructions.append(('dont', match.start(), None))
    
    # Sort instructions by position
    instructions.sort(key=lambda x: x[1])
    
    # Process instructions in order
    results = []
    enabled = True  # Multiplications are enabled by default
    
    for inst_type, _, value in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            results.append(value)
    
    return results

def main():
    # Read input
    memory = read_input()
    
    if not memory:
        return
    
    # Part 1: Find and calculate all valid multiplications
    results = find_valid_multiplications(memory)
    
    # Sum all results
    total = sum(results)
    print(f"Sum of enabled multiplication results: {total}")

if __name__ == "__main__":
    main()
