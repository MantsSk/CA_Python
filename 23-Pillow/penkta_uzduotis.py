from PIL import Image
import os

def turn_binary(img, r, g, b):
    img = Image.open(img)
    data = img.getdata()
    new_data = []
    black = 0, 0, 0
    white = 255, 255, 255
    for pixel in data:
        if pixel[0] >= r or pixel[1] >= g or pixel[2] >= b:
            new_data.append(black)
        else:
            new_data.append(white)
    
    img.putdata(new_data)
    return img

image = turn_binary('dog.jpg', 255, 255, 8)
image.show()