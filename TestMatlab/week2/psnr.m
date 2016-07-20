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
