function [ robot ] = robotInit( robotName, robotType, portNumber )
%ROBOTINIT    Initializes the robot
%   ROBOTINIT initializes the robot for use with other commands. 
%   It is used as follows: robot = robotInit(robotName, robotType)
%
%   robotName is a string, i.e. 'broodwich', 'madonna', 'samir'
%   robotType is a string depending on the robot type, and can be 'irobot',
%   'virtual','aibo','rovio'
%
%   Note that the virtual robot is a special case. It requires the
%   portNumber as well, and is invoked as 
%   robot = robotInit('localhost','virtual',8000);
%
%   Example:
%       robot = robotInit('madonna','rovio');
%
%   This initializes the robot madonna and stores the identifier in
%   robot. Future commands are called using the variable robot, i.e.,
%   robotTurn(robot,180);

if strcmp(robotType,'irobot')
    if nargin == 3
        robot = irobotInit(robotName,portNumber);
    else
        robot = irobotInit(robotName);
    end
    %irobotSetMode(robot,'all');
    robot.type = 'irobot';
elseif strcmp(robotType,'virtual')
    robot = irobotInit(robotName,portNumber);
    robot.type = 'virtual';
elseif strcmp(robotType,'aibo')
    robot = aiboConnect(robotName);
    robot.type = 'aibo';
elseif strcmp(robotType,'rovio')
    robot = rovio(robotName);
    robot.type = 'rovio';
else
    robot = {};
    fprintf('\nError, invalid robot type parameter given\n\n');
end
