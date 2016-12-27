function [ songno ] = robotAddSong( robot, songstring )
%ROBOTADDSONG   Adds a song to the robot, if possible
%   ROBOTADDSONG adds a song to the robot. Usage is unique for each type of
%   robot.
%
%   iRobot: 
%       songno = robotAddSong(robotID,songstring);
%       robotID is the ID returned by robotInit
%       songstring is the string of notes that you want the robot to play,
%       i.e., a C major scale would be 'cdefgabc'.
%       songno is an identifier that stores the song ID for use with
%       robotPlaySong
%
%   Virtual Robot:
%       songno = robotAddsong(robotID,songwav);
%       robotID is the ID returned by robotInit
%       songwav is the filename of a .wav file that you want to play. This
%       is stored in Matlab, not in the actual virtual robot.
%       songno is a struct that you use when calling robotPlaySong
%
%   Aibo:
%       For adding a song on the Aibo, you need to physically put the .wav
%       file on the memory card. Ask a course consultant to do this for
%       you.
%
%   Rovio:
%       The Rovio can not play songs using Matlab. The manual says you have
%       to be using Internet Explorer on a PC. Feel free to experiment with
%       this.
robotType = robot.type;
if strcmp(robotType,'irobot')
    songno = irobotAddSong(robot,songstring);
elseif strcmp(robotType,'virtual')
    [wav freq] = wavread(songstring);
    songno.wav = wav;
    songno.freq = freq;
elseif strcmp(robotType,'aibo')
    songno = 999;
    fprintf('\nThe Aibo can play .wav files. To add a song, give the file to a course consultant and ask them to put it on the Aibos memory stick.\n\n');
elseif strcmp(robotType,'rovio')
    songno = 999;
    fprintf('\nTo play a song with the Rovio, you have to be using Internet Explorer on a PC. You are free to experiment with this using your own computer. Ask a course consultant if you have questions.\n\n');
else
    songno = 999;
    fprintf('\nError, invalid robot\n\n');
end

