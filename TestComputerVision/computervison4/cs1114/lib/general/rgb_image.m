function I = rgb_image(r, g, b)

[rows, cols] = size(r);

I = zeros(rows, cols, 3);
I(:,:,1) = r;
I(:,:,2) = g;
I(:,:,3) = b;
