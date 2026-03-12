from PIL import Image

def test():
    img = Image.open('ouija.webp')
    w, h = img.size
    print(f"Image size: {w}x{h}")
    # Crop a sample region around A
    # A is supposedly at 17% x, 20.5% y
    cx, cy = int(w * 0.17), int(h * 0.205)
    print(f"'A' point: {cx}, {cy}")
    
test()
