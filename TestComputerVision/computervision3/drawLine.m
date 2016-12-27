function [] = drawLine(inputline, img, col)

% Input - inputline: a 3x1 vector that contains homogeneous coordinates of line
%         img      : the image on which you want to plot the line
%         col      : the color you want to use for the line
%
% Author - Manmohan Chandraker
% Date   - May 18, 2006


%  Execute the following commands before plotting the lines: 
%  figure; imshow(r,[]); axis image; hold on;
          
  % Shuffle parameters for Matlab window
  b = inputline(1);
  a = inputline(2);
  c = inputline(3);
  
  % Flip Matlab window size for bounding box
  [cols,rows] = size(img);
  flag = 1;
  cp = zeros(2,2);

  % Determine intersections with bounding box
  p1 = -(b+c)/a;
  p2 = -(a+c)/b;
  p3 = -(b * cols + c)/a;
  p4 = -(a * rows + c)/b;

  % Keep track of number of intersections and corresponding edge
  if (flag <= 2 & p1 >= 1 & p1 <= rows)
    cp(flag,:) = [p1,1];
    flag = flag + 1;
  end

  if (flag <= 2 & p2 >= 1 & p2 <= cols)
    cp(flag,:) = [1,p2];
    flag = flag + 1;
  end

  if (flag <= 2 & p3 >= 1 & p3 <= rows)
    cp(flag,:) = [p3,cols];
    flag = flag + 1;
  end

  if (flag <= 2 & p4 >= 1 & p4 <= cols)
    cp(flag,:) = [rows,p4];
    flag = flag + 1;
  end

  % Plot the line (temp variable for loop extension)
  cptemp = cp;
  line([cptemp(1,1) cptemp(2,1)], [cptemp(1,2) cptemp(2,2)], 'color', col);

