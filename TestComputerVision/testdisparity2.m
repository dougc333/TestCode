left=rgb2gray(imread('scene_left.png'));
right=rgb2gray(imread('scene_right.png'));

figure;subplot(1,2,1);imshow(left);title('left');subplot(1,2,2);imshow(right);title('right');

%can create single image with cyan 

disparityRange = [-6 10];
disparityMap = disparity(left,right,'BlockSize',15,'DisparityRange',disparityRange);

figure
imshow(disparityMap, disparityRange);
title('Disparity Map');
colormap jet
colorbar
