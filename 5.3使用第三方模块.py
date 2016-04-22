#coding=utf-8

"""
Pillow用来处理图像

"""

from PIL import Image
im=image.open("test.png")
print(im.format,im.size,im.mode)
PNG (400,300) RGB
im.thumbnail(200,100)