import re

with open('script.js', 'r') as f:
    text = f.read()

with open('new_map.txt', 'r') as f:
    new_map = f.read()

# Fix the escaping issues in new_map
new_map = new_map.replace("{ char: '\',", "{ char: '\\\\',")
new_map = new_map.replace("{ char: ''',", "{ char: '\\'',")

# Replace CHAR_MAP array in script.js
pattern = r"const CHAR_MAP = \[.*?\];"
replacement = "const CHAR_MAP =" + new_map + ";"

new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

with open('script.js', 'w') as f:
    f.write(new_text)

print("Map updated.")
