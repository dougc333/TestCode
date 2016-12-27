%{
Copyright 2009 Stephen McGill, John Schaeffer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
%}


%% Code written by Stephen McGill (c) 2009
%% Used for Independent Study Course 
%% at University of Pennsylvania 
%% with Professor Kostas Daniilidis

classdef rovio
    %ROVIO
    %   Detailed explanation goes here
    
    properties
        rovio_host = ' ';
        type = 'rovio';
    end
    
    methods
        function obj = rovio( host )
            obj.rovio_host = host;
        end
        
        function [ grabbed ] = grab_image( obj )
            %grab_image This function grabs Rovio's current image
            url = strcat('http://', obj.rovio_host,'/Jpeg/CamImg1234.jpg');
            grabbed = imread( url );
        end
        
        function [ img1 img2 ] = grab_image_pair( obj )
            %grab_image This function grabs Rovio's current image
            url_pic = strcat('http://', obj.rovio_host,'/Jpeg/CamImg1234.jpg');
            img1 = imread( url_pic );
            %Go right
            for i=1:5
            move( obj, 4, 5 );
            end
            pause(1);
            %capture slave image
            img2 = imread( url_pic );
            %Come back
            for i=1:5
            move( obj, 3, 5 );
            end
        end
        
        function [ response ] = turnLeft( obj, num, speed )
            for i=1:num
                response = move( obj, 5, speed );
            end
        end
        
        function [ response ] = turnRight( obj, num, speed )
            for i=1:num
                response = move( obj, 6, speed );
            end
        end
        
        function [ response ] = goForward( obj, num )
            for i=1:num
                response = move( obj, 1, 6 );
            end
        end
        
        function [ response ] = move( obj, dir, speed )
            % Directions
            % 0 (Stop)
            % 1 (Forward)
            % 2 (Backward)
            % 3 (Straight left)
            % 4 (Straight right)
            % 5 (Rotate left by speed)
            % 6 (Rotate right by speed)
            % 7 (Diagonal forward left)
            % 8 (Diagonal forward right)
            % 9 (Diagonal backward left)
            % 10 (Diagonal backward right)
            % 11 (Head up)
            % 12 (Head down)
            % 13 (Head middle)
            % 17 (Rotate left by 20 degree angle increments)
            % 18 (Rotate right by 20 degree angle increments
            
            url = strcat('http://',obj.rovio_host,...
                         '/rev.cgi?Cmd=nav&action=18&drive=',...
                         num2str(dir),'&speed=',num2str(speed) );
            s = urlread(url);
            response = str2num( s( findstr('responses', s) + 12 ) );
        end
        
        function [ response ] = go_home(obj)
            url = strcat('http://',obj.rovio_host,...
                         '/rev.cgi?Cmd=nav&action=13');
            s = urlread(url);
            response = str2num( s( findstr('responses', s) + 12 ) );
        end
        
        function [ status ] = get_MCU( obj )
            %GET_MCU retrieves motion control state information
            url = strcat('http://',obj.rovio_host,'/rev.cgi?Cmd=nav&action=20');
            s = urlread( url );
            i = findstr('responses', s) + 12;
            hex_result = s(i:i+29);
            
            %disp(hex_result);
            
            % MCU
            % 1 (Length of Packet)
            % 2 (Not in use)
            % 3 (Left Wheel Direction)<-Bit 2
            % 4 (Number of Left Encoder ticks)
            % 5 (Right Wheel Direction)<-Bit2
            % 6 (Number of Right Encoder Ticks)
            % 7 (Rear Wheel Direction)<-Bit2
            % 8 (Number of Rear Encoder Ticks)
            % 9 (Not in Use)
            % 10 (Head Position)
            % 11 (Battery)
            % 12 (Light and IR)
            
            status = zeros(12,1);
            status(1) = hex2dec( hex_result(1:2) );
            status(2) = hex2dec( hex_result(3:4) );
            
            str = dec2bin( hex2dec(hex_result(5:6)), 8 );
            status(3) = str2double(str(6));
            status(4) = hex2dec( hex_result(7:10) );
            str = dec2bin( hex2dec(hex_result(11:12)), 8);
            status(5) = str2double(str(6));
            status(6) = hex2dec( hex_result(13:16) );
            str = dec2bin( hex2dec(hex_result(17:18)), 8);
            status(7) = str2double(str(6));
            
            status(8) = hex2dec( hex_result(19:22) );
            status(9) = hex2dec( hex_result(23:24) );
            status(10) = hex2dec( hex_result(25:26) );
            status(11) = hex2dec( hex_result(27:28) );
            status(12) = hex2dec( hex_result(29:30) );
        end
        
        % NOTE: function modified by John Schaeffer, 2009
        function [ x, y, theta, room ] = get_Report( obj )
            url = strcat('http://',obj.rovio_host,'/rev.cgi?Cmd=nav&action=1');
            s = urlread( url );
            %disp( s );
            resp = str2num( s( findstr('responses', s) + 12 ) );
            if (resp~=0)
                disp('ERROR!');
            end
            x1 = findstr('x=', s) + 2;
            x2 = findstr('|y=', s) - 1;
            x = str2double( s(x1:x2) );
            y1 = x2+4;
            y2 = findstr('|theta=', s) - 1;
            y = str2double( s(y1:y2) );
            t1 = y2+8;
            t2 = findstr('|room=', s) - 1;
            theta = str2double( s(t1:t2) );
            r1 = t2 + 7;
            r2 = findstr('|ss=', s) - 1;
            room = str2double(s(r1:r2));
        end
        
        function [xdelta ydelta] = get_delta(obj)
            [x y theta] = get_Report(obj);
            
            %Get encoder stuff
            encoders = get_MCU(obj);
            A_enc = encoders(4);
            B_enc = encoders(6);
            C_enc = encoders(8);
            A_enc_dir = logical( encoders(3) );
            B_enc_dir = logical( encoders(5) );
            C_enc_dir = logical( encoders(7) );

            xish = (A_enc_dir==B_enc_dir)*(2*A_enc_dir-1)*(A_enc+B_enc)/2; % Have to be in the same direction, please
            yish = (A_enc_dir~=B_enc_dir&&A_enc_dir~=C_enc_dir)*(2*C_enc_dir-1)*C_enc; % There is no pure strafe if a and b move

            if( A_enc_dir==B_enc_dir )
                xdelta = xish*cos(theta);
                ydelta = xish*sin(theta);
            else
                xdelta = yish*sin(theta);
                ydelta = yish*cos(theta);
            end
        end
        
    end
    
end

