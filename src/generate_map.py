import json

def generate_arc(chars, start_x, end_x, arch_y_middle, arch_y_ends, w, h):
    map_data = []
    n = len(chars)
    for i, char in enumerate(chars):
        if n > 1:
            fraction = i / (n - 1)
        else:
            fraction = 0.5
            
        x = start_x + (end_x - start_x) * fraction
        
        mid_x = (start_x + end_x) / 2
        dx = start_x - mid_x
        a = (arch_y_ends - arch_y_middle) / (dx * dx) if dx != 0 else 0
        y = a * (x - mid_x)**2 + arch_y_middle
        
        map_data.append({
            "char": char,
            "x": round(x, 1),
            "y": round(y, 1),
            "w": w,
            "h": h
        })
    return map_data

all_chars = []

# Row 1: A-M
row1 = list("ABCDEFGHIJKLM")
all_chars.extend(generate_arc(row1, start_x=28.0, end_x=69.0, arch_y_middle=31.0, arch_y_ends=35.0, w=3.5, h=6.5))

# Row 2: N-Z
row2 = list("NOPQRSTUVWXYZ")
all_chars.extend(generate_arc(row2, start_x=28.0, end_x=69.0, arch_y_middle=41.5, arch_y_ends=44.0, w=3.5, h=6.5))

# Row 3: Numbers 0-9
row3 = list("0123456789")
all_chars.extend(generate_arc(row3, start_x=36.0, end_x=62.0, arch_y_middle=52.0, arch_y_ends=52.0, w=3.5, h=6.5))

# Row 4: Punctuation 1
punc1 = ['-', '+', '/', '|', '\\', ':', ';', '<', '_', '>', '?', '!', '.', ',', '@', '%', '&']
all_chars.extend(generate_arc(punc1, start_x=31.0, end_x=65.0, arch_y_middle=65.0, arch_y_ends=65.0, w=2.5, h=4.5))

# Row 5: Punctuation 2
punc2 = ['#', '*', "'", '(', '~', ')', '"', '$', '€', '£', '¥']
all_chars.extend(generate_arc(punc2, start_x=38.0, end_x=53.0, arch_y_middle=74.0, arch_y_ends=74.0, w=2.5, h=4.5))

# Words
all_chars.append({"char": "THE", "x": 57.0, "y": 72.0, "w": 4.0, "h": 4.5})
all_chars.append({"char": "AND", "x": 62.0, "y": 72.0, "w": 4.0, "h": 4.5})

js_str = " [\n"
for c in all_chars:
    char_str = c['char']
    if char_str == '\\': char_str = "\\\\"
    if char_str == "'": char_str = "\\'"
    js_str += f"    {{ char: '{char_str}', x: {c['x']}, y: {c['y']}, w: {c['w']}, h: {c['h']} }},\n"
js_str += "  ]"

import re
with open('script.js', 'r') as f:
    text = f.read()
pattern = r"const CHAR_MAP = \[.*?\];"
replacement = "const CHAR_MAP =" + js_str + ";"
new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)
with open('script.js', 'w') as f:
    f.write(new_text)
