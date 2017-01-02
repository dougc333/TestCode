%median filtering noisy image


%http://www.mathworks.com/help/matlab/creating_plots/working-with-8-bit-and-16-bit-images.html
%lots of incorrect links on double/uint8
noisyImg = im2double(imread('/Users/dc/TestCode/TestMatlab/hw5noisy.jpg'))
checkImg=uint8(round(noisyImg*255))
checkImg16=uint16(round(noisyImg*65535))
%showImg=imshow(checkImg)

medImg1=medfilt2(noisyImg)
showImg=imshow(medImg1)



