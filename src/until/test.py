import pytesseract
from PIL import Image

image = Image.open(r"E:\imooc\xxxx.png")
code = pytesseract.image_to_string(image, lang="chi_sim+eng", config="--psm 9")
print(code)
