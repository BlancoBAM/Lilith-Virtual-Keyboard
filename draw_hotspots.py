import json
from PIL import Image, ImageDraw
import re

# Read the HTML script to parse coordinates
with open('script.js', 'r') as f:
    text = f.read()

# Extract CHAR_MAP objects using basic regex
# matches { char: 'A', x: 17.0, y: 20.5, w: 4.5, h: 6.5 }
pattern = r"\{ char:\s*'([^']+)',\s*x:\s*([\d.]+),\s*y:\s*([\d.]+),\s*w:\s*([\d.]+),\s*h:\s*([\d.]+)\s*\}"
matches = re.findall(pattern, text)

img = Image.open('ouija.webp').convert('RGB')
draw = ImageDraw.Draw(img)
w, h = img.size

for match in matches:
    char, x, y, cw, ch = match
    x, y, cw, ch = float(x), float(y), float(cw), float(ch)
    
    px = int(w * (x / 100))
    py = int(h * (y / 100))
    pw = int(w * (cw / 100))
    ph = int(h * (ch / 100))
    
    draw.rectangle([px, py, px+pw, py+ph], outline="red", width=2)
    # Draw center dot where planchette should go
    cx, cy = px + pw/2, py + ph/2
    draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill="lime")

img.save('debug.jpg')
print("Saved debug.jpg")
