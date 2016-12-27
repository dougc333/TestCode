function [pts] = clickPoints(img, n, plot_status, label_status)

% Function to select points in an image using a mouse-click
% The coordinates of the points are returned in the arrays X and Y
%
% Inputs -  img          : The input image
%           n            : Number of points to be clicked
%           plot_status  : If 1, the clicked points are marked by a red +
%           label_status : If 1, the clicked points are numbered in order
%
% Output -  pts  : (x,y)-coordinates of the n clicked points
%
% Author - Manmohan Chandraker
% Date   - May 18, 2006


figure; imshow(img,[]); axis image; hold on;
title('Input Image');
X = [];
Y = [];
for i=1:n
    [px py] = ginput(1);
    X = [X , py];
    Y = [Y , px];
    if plot_status == 1
        plot( px, py, 'r+' );
    end
    if label_status == 1
        h = text( px+5, py, num2str(i) );
        set(h,'Color',[0 1 0]);
    end
end

pts = [X;Y];

