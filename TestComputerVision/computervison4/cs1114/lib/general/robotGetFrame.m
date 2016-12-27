function [ image ] = robotGetFrame( robot )
%ROBOTGETFRAME  Gets an image from the robot camera
%   ROBOTGETFRAME uses the camera on the robot to obtain an image in the
%   form of a three dimensional matrix. It is used as follows:
%   img = robotGetFrame(robotID);
%
%   The robotID is the variable returned by robotInit.
%   img is the variable name you wish to store the image in.
%
%   You can see the image returned by using the command imshow(img);.

robotType = robot.type;

if strcmp(robotType,'irobot')
    image = irobotGetFrame(robot);
elseif strcmp(robotType,'virtual')
    image = irobotGetFrame(robot);
elseif strcmp(robotType,'aibo')
    image = aiboGetFrame(robot);
elseif strcmp(robotType,'rovio')
    image = grab_image(robot);
else
    image = [];
    fprintf('\nError, invalid robot\n\n');
end
