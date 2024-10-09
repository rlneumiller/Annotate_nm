nm --print-size --size-sort --reverse-sort build/zephyr/zephyr.elf > nm.txt

# Copyright 2024 by Arrel Neumiller
# file: annotate_nm.py
# Example usage: nm --print-size --size-sort --reverse-sort build/zephyr/zephyr.elf > nm.txt

# Define the meaning of nm's single letter types with scope
type_meanings = {
    'b': 'Local uninitialized data section (BSS)',
    'B': 'Global uninitialized data section (BSS)',
    'r': 'Local read-only data section',
    'R': 'Global read-only data section',
    't': 'Local text (code) section',
    'T': 'Global text (code) section',
    'd': 'Local initialized data section',
    'D': 'Global initialized data section',
    'u': 'Unique global symbol',
    'U': 'Undefined symbol',
    'v': 'Weak object symbol',
    'V': 'Weak object symbol',
    'w': 'Weak symbol',
    'W': 'Weak symbol',
    'a': 'Absolute symbol',
    'A': 'Absolute symbol',
    'n': 'Debugging symbol',
    'N': 'Debugging symbol',
    'i': 'Indirect reference to another symbol',
    'I': 'Indirect reference to another symbol',
    'p': 'Stack unwind section',
    'P': 'Stack unwind section',
    'o': 'Small object',
    'O': 'Small object'
}

# Read the nm.txt file
with open('nm.txt', 'r') as file:
    lines = file.readlines()

# Define the fixed distance from the left margin for the type annotation column
fixed_distance = 80

# Process each line and add annotations
annotated_lines = []
for line in lines:
    parts = line.split()
    if len(parts) < 4:
        continue

    address = parts[0]
    size_hex = parts[1]
    type_letter = parts[2]
    symbol_name = parts[3]

    # Convert size from hex to decimal
    size_decimal = int(size_hex, 16)

    # Get the meaning of the type letter
    type_meaning = type_meanings.get(type_letter, 'Unknown type')

    # Create the annotated line with aligned type annotation
    base_info = f"{address} {size_hex} ({size_decimal} bytes) {symbol_name}"
    padding = ' ' * (fixed_distance - len(base_info))
    annotated_line = f"{base_info}{padding}{type_letter} ({type_meaning})"
    annotated_lines.append(annotated_line)

# Write the annotated lines to a new file
with open('nm_annotated.txt', 'w') as file:
    file.write('\n'.join(annotated_lines))

print("Annotated file 'nm_annotated.txt' has been created.")
