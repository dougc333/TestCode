% Connected component exploration algorithm
% Author: Will Chang


function marked = explore(image)
%
%  image is a 2D array that contains values (zeros and ones)
%  corresponding to the binarized image.
%

s = size(image);
width = s(1); height = s(2);

marked = zeros(width, height);			% marked image
marker = 0;								% marker index

% keep a stack of pixel locations that we need to explore
stack = zeros(width*height, 2);
topStack = 0;

for i=1:width
	for j=1:height
		if ((image(i,j) == 1) && (marked(i,j) == 0))
			marker = marker + 1;

			% push the current location on the stack
			topStack = topStack + 1;
			stack(topStack, 1) = i;
			stack(topStack, 2) = j;
			
			% use a stack to emulate recursion
			while (topStack > 0)
				nx = stack(topStack, 1);	% x-coordinate of neighbor
				ny = stack(topStack, 2);	% y-coordinate of neighbor
				topStack = topStack - 1;
				
				if ((image(nx, ny) == 1) && (marked(nx, ny) == 0))
					marked(nx, ny) = marker;
					% iteratively explore the connected components
					% I'm assuming 8-connectedness here
					for x=-1:1
						for y=-1:1
							% push the neighbor on the stack... only if
							% pixel coordinates are inside the boundaries
							if ((nx+x >= 1) && (nx+x <= width) &&...
								(ny+y >= 1) && (ny+y <= height))
								topStack = topStack + 1;
								stack(topStack, 1) = nx+x;
								stack(topStack, 2) = ny+y;
							end
						end
					end
				end
			end
		end
	end
end
