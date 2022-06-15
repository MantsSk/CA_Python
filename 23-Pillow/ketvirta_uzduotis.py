from PIL import Image
import os

def ribos(sk):
    if sk < 0:
        return 0
    elif sk > 255:
        return 255
    return sk


def adjust_colors(img, r, g, b):
    img = Image.open(img)
    data = img.getdata()
    new_data = []
    for pixel in data:
        red = ribos(pixel[0] + r)
        green = ribos(pixel[1] + g)
        blue = ribos(pixel[2] + b)
        new_pixel = (red, green, blue)
        new_data.append(new_pixel)
    
    img.putdata(new_data)
    return img

new_img = adjust_colors('dog.jpg', 0, 0 , +80)
new_img.show()