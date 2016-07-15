%hw1a 

%given matrix, vectorize matrix

%test_mat = [1 2 3;4 5 6;7 8 9]

%
%vec_row1 = test_mat(1,:)
%
%vec_col1 = test_mat(:,1)
%
%vec_mat = test_mat(:)
%size(vec_mat)

%vec_reshape_row = reshape(test_mat,1,[])
%vec_reshape_column= reshape(test_mat,[],1)


BASE_PATH='/Users/dc/TestCode/TestMatlab/computervision3/';

img =im2double(imread(strcat(BASE_PATH,'rectangles.jpg')));
[M,N] = size(img); figure(1);
hold on;
line([10,10],[20,20],'Color','w','LineWidth',2);
%alpha = alpha(1:M, 1:N); 
%set(img, 'AlphaData', alpha);
imshow(img);
hold off;
%test=reshape(img,[],1)
numUnique=unique(img);
%default is 10 bins
h=hist(reshape(img,[],1))

%what does 20 bins look like? 
h1 = hist(reshape(img,[],1),20);
[N, edges] = histcounts(img)

[row, col]=find(img == img(1,1))


%A(1:255,1:255)= .9020;figure(2); imshow(A)
%[row, col]=find(A == .9020)

%B(1:255,1:255)=.6;figure(3);imshow(B)
%C(1:255,1:255)=.4510;figure(4);imshow(C)
%testMe = img < .1;
%a = unique(testMe)
%nnz(testMe)n,1)
%b = ismember(testMe,[1]);
%row vector containing size of each column
%s=sum(b)
%num_ones =sum(sum(b)) 

