function [] = robotTurn(robot,degrees)
%ROBOTTURN Robot turns the desired number of degrees
%   ROBOTTURN commands the robot to turn the given degree measure. It is
%   used as follows: robotTurn(robotID, degrees);
%
%   The robotID is the variable returned by robotInit.
%   The degrees parameter is how many degrees you want the robot to turn,
%   i.e. 180 has the robot turn around. Positive degrees are clockwise and
%   negative degrees are counter-clockwise.
%
%   Special notes: This command is non-blocking for the irobot and virtual
%   robot, and blocking for the aibo and rovio. Blocking means that it
%   pauses until the robot is done, and no further commands can be issued
%   or accepted until this command is complete. This implies that you have
%   to make your own pause statements when using the irobot or virtual
%   robot.
%
%   The Aibo can only turn accurate up to 35 degrees, so any input 
%   angle will be rounded to the nearest usable angle.
%
%   The Rovio is only accurate to 20 degree increments. However, this seems
%   to be accurate enough for most things you'll want to do with it.

robotType = robot.type;
if strcmp(robotType,'irobot')
    irobotTurn(robot,degrees);
elseif strcmp(robotType,'virtual')
    irobotTurn(robot,degrees);
elseif strcmp(robotType,'aibo')
    %Aibo can only move CCW, so any degree turns must be negative
    if degrees > 0
        v = -5;
    else
        v = 5;
    end
    degrees = abs(degrees);
    %It takes roughly 4.5 seconds for one full rotation. Speed doesn't seem to affect the actual rate.
    %Minimum possible turn is 35 degrees. Linear relationship for degrees > 90 with respect to time. 
    if degrees > 175 || degrees == 90
        time = 0.5 + 0.5*round(degrees/45);
        aiboTurn(robot,v);
        pause(time);
        aiboTurn(robot,0);
    else
    %Otherwise, we delay move 35 degrees and stop the necessary number of times
        delays = round(degrees/35);
        for k = 1:delays
            aiboTurn(robot,v); pause(1); aiboTurn(robot,0); pause(1.4);
        end
    end
    pause(1.5);
elseif strcmp(robotType,'rovio')
    %To simplify turns by specific degrees, we use set 20 degree intervals.
    %We can switch to a different method after we calibrate if more precision is needed.
    turns = degrees/20;
    if turns > 0
	turns = round(turns);
        dir = 18;
    else
        turns = -round(turns);
        dir = 17;
    end
    for x = 1:turns
        pause(.3);
        response = move( robot, dir, 6 ); 
    end
else
    fprintf('\nError, invalid robot\n\n');
end
