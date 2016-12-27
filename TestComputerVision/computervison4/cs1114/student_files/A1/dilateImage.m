function output = dilateImage(input)
% Take a grayscale image 'input' and "dilate" it by replacing each pixel's
% intensity with the highest intensity in its neighborhood (where the
% "neighborhood" includes itself, and it's four neighbors: up, down, left,
% and right).  What you do on the boundary of the image is up to you.  
% The output image will be returned in the matrix 'output'.
