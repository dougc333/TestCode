function [R,G,B] = image_rgb(img)
  R = img(:,:,1);
  G = img(:,:,2);
  B = img(:,:,3);
end
