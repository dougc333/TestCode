function img = im2double(img)
% Returns the input image converted to double in range [0-1]
%
% Assumes the input image is uint8 in the range [0-255] or already 
%     an appropriate double image in the range [0-1]

if(~isequal(class(img), 'double'))
    img = double(img) ./ 255;
end
if((max(max(img)) - 1.0) > 0.001)
    img = img ./ 255;
end

end
