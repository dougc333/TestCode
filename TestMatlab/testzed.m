clear all; close all; clc;

zed=webcam(3);

% set the desired resolution
zed.Resolution = zed.AvailableResolutions{1};
% get thhe image size
[height width cfhannels] = size(snapshot(zed))
  
% Create Figure and wait for keyboard interruption to quit
f = figure('keypressfcn','close','windowstyle','modal');
ok = 1;
% loop over frames
while ok
    %capture the current image
    img = snapshot(zed);
      
    % split the side by side image image into two images
    im_Left = img(:, 1 : width/2, :);
    im_Right = img(:, width/2 +1: width, :);
      
    % display the left and right images
    subplot(1,2,1);
    imshow(im_Left);
    title('Image Left');
    subplot(1,2,2);
    imshow(im_Right);
    title('Image Right');
      
    drawnow; %this checks for interrupts
    ok = ishandle(f); %does the figure still exist
end
  
% close the camera instance
clear cam


