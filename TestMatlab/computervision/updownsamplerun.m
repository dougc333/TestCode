


img=imread('/Users/dc/TestCode/TestMatlab/computervision/updownsample.jpg')
imgdouble = im2double(img)
%lpf imgdouble
lpf=[(1/9) (1/9) (1/9); (1/9) (1/9) (1/9); (1/9) (1/9) (1/9)]
imgdoublpf=imfilter(imgdouble,lpf,'replicate')
imgsmall=imgdoublpf(1:2:end,1:2:end)
z=zeros(359,479)
for i=1:359
    for j=1:479
        if(mod(i,2)==1 && mod(j,2)==1)
            fprintf ('i:%d j:%d \n',i,j)
            z(i,j)=imgsmall((i+1)/2,(j+1)/2);
        end
    end
end
bilinear=[0.25,0.5,0.25;0.5,1,0.5;0.25,0.5,0.25]
res=imfilter(z,bilinear)

dist=abs(res-imgdouble).^2
mse=sum(dist(:))/numel(imgdouble)
psnr=10*log10(255^2/mse)

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
   
%example for up/down sampling
%gaussian/laplace pyramid




