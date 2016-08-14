#!/usr/bin/python
from PIL import Image, ImageDraw
import scipy.misc
from scipy.ndimage import sobel
import numpy
from scipy import ndimage

im=Image.open('/Users/dc/Desktop/IMG_1400.jpg')
#im.show()
(N,M)=im.size


draw=ImageDraw.Draw(im)
#TOP
draw.line((0,1459,2448,1449),fill=128)
draw.line((0,1460,2448,1450),fill=128)
#BOTTOM
draw.line((0,1490,2448,1490),fill=128)
draw.line((0,1491,2448,1491),fill=128)
#LEFT
draw.line((1160,0,1160,3264),fill=128)
draw.line((1161,0,1161,3264),fill=128)
#RIGHT
draw.line((1190,0,1190,3264),fill=128)
draw.line((1191,0,1191,3264),fill=128)

del draw
im.save('/Users/dc/TestCode/TestBear/redline.jpg')
im.show()

#crop
#test=img.crop((1160,1460,1190,1490))
#test.show() #verifies as only bear in 30x30

#test sobel
im2=scipy.misc.imread('/Users/dc/Desktop/IMG_1400.jpg')
im2=im2.astype('int32')
dx=ndimage.sobel(im2,1)
dy=ndimage.sobel(im2,0)
mag = numpy.hypot(dx,dy)
mag *= 255.0/numpy.max(mag)
im.show()



