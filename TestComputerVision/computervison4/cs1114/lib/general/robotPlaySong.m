function [] = robotPlaySong( robot, songno )
%ROBOTPLAYSONG  Robot plays the specified song
%   ROBOTPLAYSONG tells the robot to play the given song. Usage is unique
%   for each robot.
%
%   iRobot and Virtual Robot:
%       robotPlaySong(robotID, songno);
%       robotID is the ID returned by robotInit
%       songno is the identifier returned by robotAddSong
%
%   Aibo:
%       robotPlaySong(robotID,songName);
%       robotID is the ID returned by robotInit
%       songName is the title of the .wav file put on the card, 
%       i.e. 'bark.wav'
%
%   Rovio:
%       The Rovio can not play songs using Matlab. The manual says you have
%       to be using Internet Explorer on a PC. Feel free to experiment with
%       this.

robotType = robot.type;
if strcmp(robotType,'irobot')
    irobotPlaySong( robot, songno );
elseif strcmp(robotType,'virtual')
    wavplay(songno.wav,songno.freq);
elseif strcmp(robotType,'aibo')
    aiboPlaySound(robot,songno);    
elseif strcmp(robotType,'rovio')
    fprintf('\nTo play a song with the Rovio, you have to be using Internet Explorer on a PC. You are free to experiment with this using your own computer. Ask a course consultant if you have questions.\n\n');
else
    fprintf('\nError, invalid robot\n\n');
end

