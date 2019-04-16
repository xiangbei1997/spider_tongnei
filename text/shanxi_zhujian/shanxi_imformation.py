from PIL import Image
import pytesseract
zz = pytesseract.image_to_string(Image.open('captcha.png'))
print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
print(zz)