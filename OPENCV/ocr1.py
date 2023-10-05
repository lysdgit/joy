from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open( r'C:\Users\liys2\Desktop\22.png'))
 
print(text)