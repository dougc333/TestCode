%histogram.m

img=im2double(imread('/Users/dc/TestCode/TestMatlab/tire.tif'));

figure; subplot(1,2,1);imshow(img); title('tire');subplot(1,2,2);imhist(img);

%does histogram equalization help in random forest?

figure;subplot(1,2,1); imshow(histeq(img));subplot(1,2,2); imhist(histeq(img));


