function [ output ] = getCeiling
% GETCEILING fetches a frame from the ceiling camera in Upson 317


% use this if the camera no longer needs basic auth
%    output = imread('http://camera1/IMAGE.JPG');

% use this if the camera is behind basic auth
import javax.imageio.*
 
url = java.net.URL('http://camera1/image.jpg');
uc = url.openConnection();
uc.setRequestProperty('Authorization', 'Basic cm9ib2Rhd2c6'); % robodawg:
uc.connect();
is = uc.getInputStream();

dst = ImageIO.read(is);

% convert Java image into Matlab image
H = dst.getHeight;
W = dst.getWidth;
output = uint8(zeros([H,W,3]));
pixelsData = uint8(dst.getData.getPixels(0,0,W,H,[]));
for i = 1 : H
    base = (i-1)*W*3+1;
    output(i,1:W,:) = deal(reshape(pixelsData(base:(base+3*W-1)),3,W)');
end

