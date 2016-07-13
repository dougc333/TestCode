%hw1a 

%given matrix, vectorize matrix

test_mat = [1 2 3;4 5 6;7 8 9]

%
vec_row1 = test_mat(1,:)
%
vec_col1 = test_mat(:,1)
%
vec_mat = test_mat(:)
size(vec_mat)

vec_reshape_row = reshape(test_mat,1,[])
vec_reshape_column= reshape(test_mat,[],1)


BASE_PATH='/Users/dc/TestCode/TestMatlab/computervision3/';

img =im2double(imread(strcat(BASE_PATH,'blocks1.gif')));
imshow(img);
%test=reshape(img,[],1)

hist(reshape(img,[],1))

%compute histogram and use it to segment images!!






