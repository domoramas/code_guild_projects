#image manipulation
from PIL import Image
# import PIL

img = Image.open("/Users/damianoramas/Desktop/redmage/class_redmage/code/dom/Lenna_(test_image).png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y =round(0.299*r + 0.587*g + 0.114*b)
        r =y
        g =y
        b =y


        pixels[i, j] = (r, g, b)
img.show()