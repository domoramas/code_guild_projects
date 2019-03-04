#image manipulation
from PIL import Image
# import PIL
import colorsys

img = Image.open("/Users/damianoramas/Desktop/redmage/class_redmage/code/dom/Lenna_(test_image).png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        #print (h,s,v)
        h *= 20
        s *= 1
        v *= 1
         #print(h,s,v)

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)
img.show()