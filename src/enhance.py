# Scientific & Imaging Libraries

import numpy as np
import PIL.Image as img

im = img.open("test.jpg")
new = img.new( 'RGB', (im.size[0] // 8, im.size[1] // 8), "black")
pixels = im.load()
pixnew = new.load()
for i in range(new.size[0]):
    for j in range(new.size[1]):
        r, g, b = 0, 0, 0
        for x in range(8):
            for y in range(8):
                r += pixels[8*i + x, 8*j + y][0]
                g += pixels[8*i + x, 8*j + y][1]
                b += pixels[8*i + x, 8*j + y][2]
        pixnew[i, j] = (r//64, g//64, b//64)

im.show()
new.show()