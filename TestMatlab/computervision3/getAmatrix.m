function [A] = getAmatrix(varargin)


P = path;

% Fill in the complete path for the downloaded yaleBfaces directory within the single quotes in the line below

path(P,'/Users/manu/*****/assgn4/yaleBfaces');


if nargin ~= 2
  disp('You must specify two arguments. Explicitly set to empty [] an argument you wish to exclude.');
end

col = 0;

if ~isempty(varargin{1}) & isempty(varargin{2})
  namechar1 = ['subset', num2str(varargin{1}), '/person'];
  for i = 1:10
    if i < 10
      namechar2 = ['0', num2str(i), '_'];
    else
      namechar2 = [num2str(i), '_'];
    end
  
    switch varargin{1};
      case 1
        j_range = 1:7;
      case 2
        j_range = 8:19;
      case 3
        j_range = 20:31;
      case 4
        j_range = 32:45;
      case 5
        j_range = 46:64;
      otherwise
        disp('Subset index must be between 1 and 5.');
    end

    for j = j_range(1):j_range(end)
      if j < 10
        namechar3 = ['0', num2str(j), '.png'];
      else
        namechar3 = [num2str(j), '.png'];
      end

      namechar = [namechar1, namechar2, namechar3];
      tmp_img = imread(namechar);
      A(:,col+1) = tmp_img(:);
      col = col + 1;
    end
  end

elseif ~isempty(varargin{1}) & ~isempty(varargin{2})
  namechar1 = ['subset', num2str(varargin{1}), '/person'];
  if varargin{2} < 10
    namechar2 = ['0', num2str(varargin{2}), '_'];
  else
    namechar2 = [num2str(varargin{2}), '_'];
  end

  switch varargin{1};
    case 1
      j_range = 1:7;
    case 2
      j_range = 8:19;
    case 3
      j_range = 20:31;
    case 4
      j_range = 32:45;
    case 5
      j_range = 46:64;
    otherwise
      disp('Subset index must be between 1 and 5.');
  end

  for j = j_range(1):j_range(end)
    if j < 10
      namechar3 = ['0', num2str(j), '.png'];
    else
      namechar3 = [num2str(j), '.png'];
    end

    namechar = [namechar1, namechar2, namechar3];
    tmp_img = imread(namechar);
    A(:,col+1) = tmp_img(:);
    col = col + 1;
  end

elseif isempty(varargin{1}) & isempty(varargin{2})
  for k = 1:5
    namechar1 = ['subset', num2str(k), '/person'];
    for i = 1:10
      if i < 10
        namechar2 = ['0', num2str(i), '_'];
      else
        namechar2 = [num2str(i), '_'];
      end
  
      switch k;
        case 1
          j_range = 1:7;
        case 2
          j_range = 8:19;
        case 3
          j_range = 20:31;
        case 4
          j_range = 32:45;
        case 5
          j_range = 46:64;
        otherwise
          disp('Subset index must be between 1 and 5.');
      end

      for j = j_range(1):j_range(end)
        if j < 10
          namechar3 = ['0', num2str(j), '.png'];
        else
          namechar3 = [num2str(j), '.png'];
        end

        namechar = [namechar1, namechar2, namechar3];
        tmp_img = imread(namechar);
        A(:,col+1) = tmp_img(:);
        col = col + 1;
      end
    end
  end

elseif isempty(varargin{1}) & ~isempty(varargin{2})
  for k = 1:5
    namechar1 = ['subset', num2str(k), '/person'];
    if varargin{2} < 10
      namechar2 = ['0', num2str(varargin{2}), '_'];
    else
      namechar2 = [num2str(varargin{2}), '_'];
    end
  
    switch k;
      case 1
        j_range = 1:7;
      case 2
        j_range = 8:19;
      case 3
        j_range = 20:31;
      case 4
        j_range = 32:45;
      case 5
        j_range = 46:64;
      otherwise
        disp('Subset index must be between 1 and 5.');
    end

    for j = j_range(1):j_range(end)
      if j < 10
        namechar3 = ['0', num2str(j), '.png'];
      else
        namechar3 = [num2str(j), '.png'];
      end

      namechar = [namechar1, namechar2, namechar3];
      tmp_img = imread(namechar);
      A(:,col+1) = tmp_img(:);
      col = col + 1;
    end
  end

end
