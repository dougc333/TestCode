function [] = robotDriveStraight(robot,vel,dist)
%ROBOTDRIVESTRAIGHT Drives straight at velocity vel for a distance dist
%   ROBOTDRIVESTRAIGHT commands the robot to drive straight the given
%   distance at the desired speed. It is used as follows:
%   robotDriveStraight(robotID,velocity,distance);
%   
%   The robotID is the variable returned by robotInit.
%   The velocity is a speed in mm/s, i.e. 300 is 300 mm/s = 1.08 km/h.
%   The distance is in mm, 600 is 600 mm = 60 cm, or approximately 2 feet.
%
%   Special notes: This command is non-blocking for the irobot and virtual
%   robot, and blocking for the aibo and rovio. Blocking means that it
%   pauses until the robot is done, and no further commands can be issued
%   or accepted until this command is complete. This implies that you have
%   to make your own pause statements when using the irobot or virtual
%   robot.
%
%   The Aibo has some unusual behaviour here. The aibo can only travel at
%   one speed, so the velocity parameter is ignored. If desired, the aibo
%   can be issued commands as robotDriveStraight(robotID,distance);.
%   Also, the Aibo has some trouble walking straight. For short
%   distances, it works fine, but after some time, its path starts to
%   curve.

robotType = robot.type;
if strcmp(robotType,'irobot')
    if vel > 0 && dist < 0
        vel = -vel;
    end
    irobotDriveStraight(robot,vel,dist);
elseif strcmp(robotType,'virtual')
    if vel > 0 && dist < 0
        vel = -vel;
    end
    irobotDriveStraight(robot,vel,dist);
elseif strcmp(robotType,'aibo')
    %Speed parameter doesn't seem to make any difference, so we just vary the pause time
    %For distances less than 500 mm, dog goes roughly straight, so we use one relationship
    %Distances greater than 500 mm, it starts to curve, so we have another fitted line
    if nargin == 2
        dist = vel;
    end

    if dist < 0
        v = -5;
    else
        v = 5;
    end
    
    if dist <= 500
        t = dist/93;
    else
        t = (dist - 35.814)/73.442;
    end
    aiboDriveDirect(robot,v);
    pause(t);
    aiboDriveDirect(robot,0);
    pause(1.5);
    
elseif strcmp(robotType,'rovio')
    %Speed for Rovio ranges from ~235 mm/s to 370 mm/s
    %speed 10 = 235, 8 = 253, 6 = 313, 4 = 343, 2 = 370
    if dist > 0
        dir = 1;
    else
        dist = -dist;
        dir = 2;
        if vel < 0
           vel = -vel;
        end
    end
    if vel > 356.5
        speed = 2;
        actvel = 370;
    elseif vel > 328
        speed = 4;
        actvel = 343;
    elseif vel > 283
        speed = 6;
        actvel = 313;
    elseif vel > 244
        speed = 8;
        actvel = 253;
    else
        speed = 10;
        actvel = 235;
    end
    %Each repetition of the for loop results in the car moving for roughly 0.0908 s
    reps = (dist/actvel)/0.0908;
    for x = 1:reps
       move( robot, dir,speed );
    end
else
    fprintf('\nError, invalid robot\n\n');
end
