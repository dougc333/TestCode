img=imread('/Users/dc/TestCode/TestMatlab/computervision/rgb2ind_1.png')
%image(img)
size(img)

imp1 = impyramid(img,'reduce')
size(img)
size(imp1)
image(imp1)

%lpfs and downsample
lpf=[(1/9) ]

x=-10:.1:10;
[X,Y] = meshgrid(x);
a=2; b=-3; c=10; d=-1;
%Z=(d- a * X - b * Y)/c;
Z=X*Y
surf(X,Y,Z)
shading flat
xlabel('x'); ylabel('y'); zlabel('z')

i=-20:.1:20
[I,J] = meshgrid(i);
K=I*J
%I[100,100]=7000;
%K[101,101]=7000;

surf(I,J,K)
shading flat
xlabel('i');ylabel('j');zlabel('k');

size(K)


xgv = [1 2 3];
ygv = [1 2 3 4 5];
[X,Y] = meshgrid(xgv, ygv)

[X1,X2] = ndgrid(xgv,ygv)
figure()
[X1_ndgrid,X2_ndgrid] = ndgrid(1:60,1:60);
Z = zeros(60,60);
Z(1,1)=1
Z(1,1)=2
Z(1,1)=3
Z(1,2)=3
Z(1,2)=2
Z(2,2)=1
Z(2,3)=1
Z(2,3)=2
Z(2,3)=3
Z(2,1)=3
Z(3,1)=2
Z(3,1)=1
Z(3,1)=1
Z(3,1)=2
Z(3,1)=3
Z(15,15)=3
Z(5,10)=3

%mesh(X1_ndgrid,X2_ndgrid,Z,'EdgeColor','green')
%axis equal;

% Set the axis labeling and title
%h1 = gca;
%h1.XTick = [1 2 3];
%h1.YTick = [1 2 3 4 5];
%xlabel('ndgrid Output')



figure
%bar3(Z,.01) all black, no color
bar3(Z)






