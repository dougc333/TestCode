function [ img ] = robotGetSideFrame( r )
%ROBOTGETSIDEFRAME Summary of this function goes here
%   Detailed explanation goes here

if(findstr('localhost', r.url))
     %using virtual robot
    img = robotGetFrame(r, 'rightCam');
else
   %using real robot
    img = robotGetFrame(r);
end

