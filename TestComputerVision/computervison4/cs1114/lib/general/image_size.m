function [rows,cols] = image_size(image)
  x = size(image);
  if(length(x) == 3)
    [rows,cols,depth] = size(image);
  elseif(length(x) == 2)
    [rows,cols] = size(image);
  else
    rows = 0;
    cols = 0;
  end
end
