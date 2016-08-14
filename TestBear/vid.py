#!/usr/bin/python

import pylab
import imageio
import matplotlib.pyplot as plt


filename='/Users/dc/Desktop/IMG_1397.m4v'
vid = imageio.get_reader(filename,'ffmpeg')
nums = [10,287]
for num in nums:
	image = vid.get_data(num)
	fig = plt.figure()
	plt.subtitle('image #{}'.format(num),fontsize=20)
	plt.imshow(image)
plt.show()



