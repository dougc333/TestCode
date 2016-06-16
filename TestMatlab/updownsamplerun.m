%week4
%calculate MSE between 2 matrices
X=[1 1 2 2; 1 1 2 2; 2 2 3 4; 2 2 5 6]
Y = [2 2 1 1; 2 2 2 2; 2 2 6 4; 2 2 5 3]
distxy=abs(X-Y).^2
msexy=sum(distxy(:)/numel(X))

%msexy =

%    1.5000
%MAE calculation example
mref=[10 20 10 10; 20 40 10 10; 30 40 20 20; 50 60 20 20]
m1=[10 20 10 10; 20 40 10 10; 20 20 30 40; 20 20 50 60]
m2=[20 30 20 20; 30 50 20 20; 40 50 30 30; 60 70 30 30]
m3=[10 20 30 40; 20 40 50 60; 10 10 20 20; 10 10 20 20]
m4=[1 2 1 1; 2 4 1 1; 3 4 2 2; 5 6 2 2]

dist1 = abs(mref-m1)
dist2=abs(mref-m2)
dist3 = abs(mref-m3)
dist4=abs(mref-m4)

mae1=sum(dist1(:))
mae2=sum(dist2(:))
mae3=sum(dist3(:))
mae4=sum(dist4(:))

%left off divide by 16; doesnt matter smallest valuew wins.
%mae1 =
%
%   200
%
%
%mae2 =
%
%   160
%
%
%mae3 =
%
%   280
%
%
%mae4 =
%
%   351
   

test=[1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16]
for n=1:3
for m=1:3
s=test([n:n+1],[m:m+1])
end
end

%{
s =

     1     2
     5     6


s =

     2     3
     6     7


s =

     3     4
     7     8


s =

     5     6
     9    10


s =

     6     7
    10    11


s =

     7     8
    11    12


s =

     9    10
    13    14


s =

    10    11
    14    15


s =

    11    12
    15    16
%}

I1=im2double(imread('/Users/dc/TestCode/TestMatlab/computervision/hw4frame1.jpg'))
I2=im2double(imread('/Users/dc/TestCode/TestMatlab/computervision/hw4frame2.jpg'))

Btarget=I2(65:96,81:112)
size(Btarget)

size(I1)
%mseArr[1:288]=0

for n=1:(288-32)
    for m=1:(352-32)
        s=I1([n:n+31],[m:m+31])
        dist=abs(s-Btarget)
        sum=dist(:)
        mse1=(32*32)^(-1)*sum
        %mseArr[n]=mse
    end
end

%for n:1:(288-32)
%    mseArr[n]
%end