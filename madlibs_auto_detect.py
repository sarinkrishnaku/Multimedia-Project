import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# === CONFIG ===
input_path = r"C:\Users\sarin\Desktop\Multimedia project\madlib_template.png"   # Change if your image has a different name
output_path = r"C:\Users\sarin\Desktop\Multimedia project\madlib_completed.png"
font_path = "arialbd.ttf"
font_size = 32
font = ImageFont.truetype(font_path, font_size)

# === DEBUG: Check file loading ===
print("Working directory:", os.getcwd())
print("Files:", os.listdir())

image = cv2.imread(input_path)
if image is None:
    raise FileNotFoundError(f"Image '{input_path}' not found or could not be opened.")

# === Step 1: Preprocess image ===
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# === Step 2: Detect horizontal lines ===
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=120,
                        minLineLength=100, maxLineGap=5)

# === Step 3: Filter valid blanks ===
filtered = []
tolerance = 10  # Minimum vertical distance between blanks

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(y1 - y2) < 5 and abs(x1 - x2) > 100:  # Horizontal & long enough
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            # Avoid duplicates or too-close lines
            too_close = any(abs(cy - center[1]) < tolerance for _, cy in filtered)
            if not too_close:
                filtered.append(center)

blank_positions = sorted(filtered, key=lambda p: p[1])  # Sort top to bottom

print(f"✅ Detected {len(blank_positions)} blanks.")

# === Step 4: Prompt user for words ===
user_words = []
for i in range(len(blank_positions)):
    word = input(f"Enter word for blank {i + 1}: ")
    user_words.append(word)

# === Step 5: Draw words on image ===
img_pil = Image.open(input_path).convert("RGB")
draw = ImageDraw.Draw(img_pil)
font = ImageFont.truetype(font_path, font_size)

for (x, y), word in zip(blank_positions, user_words):
    text_y = y - font_size - 5
    draw.text((x - len(word)*font_size // 4, text_y), word, font=font, fill="black")

# === Step 6: Save and show ===
img_pil.save(output_path)
img_pil.show()
print(f"🎉 MadLibs completed! Saved as '{output_path}'")