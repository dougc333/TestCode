x=randn(1,10000);
y=x';
[X,Y]=meshgrid(x,y);
z=(1000/sqrt(2*pi)*exp(-X.^2/2))
surf(x,y,z);shading interp