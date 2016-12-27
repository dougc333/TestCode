%test Ycbcr conversion and hsv conversion
%this is a b/w image, not color
[rgbImg,map]=imread('//Users/dc/TestCode/TestMatlab/computervision/lena.gif')
ycbcrImage=rgb2ycbcr(rgbImg)
hsvImage=rgb2hsv(rgbImg)
y=ycbcrImage(1,:,:)
v=hsvImage(:,:,1)