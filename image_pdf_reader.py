from PIL import Image
import pytesseract
from wand.image import Image as Img

# brew uninstall ghostscript
# brew install tesseract
with open('test.pdf', 'rb') as fd:
    with Img(file=fd, resolution=100, format="PDF[0]") as pdf:
        pdf.save(filename="sample_scan.jpg")
# with Img(filename='test.pdf', resolution=300) as img:
#     img.compression_quality = 99
#     img.format = 'pdf'
#
#     img.save(filename='sample_scan.jpg')
# No preprocessing required here as the results are fairly good.
text = pytesseract.image_to_string(Image.open('sample_scan.jpg'))
print(text)