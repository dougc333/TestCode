function varargout = part1_gui(varargin)
% PART1_GUI M-file for part1_gui.fig
%      PART1_GUI, by itself, creates a new PART1_GUI or raises the existing
%      singleton*.
%
%      H = PART1_GUI returns the handle to a new PART1_GUI or the handle to
%      the existing singleton*.
%
%      PART1_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in PART1_GUI.M with the given input arguments.
%
%      PART1_GUI('Property','Value',...) creates a new PART1_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before part1_gui_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to part1_gui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help part1_gui

% Last Modified by GUIDE v2.5 15-Jun-2006 15:23:50

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @part1_gui_OpeningFcn, ...
                   'gui_OutputFcn',  @part1_gui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT

function util_clear_ticks() 


function util_redraw_input(handles)
imagesc(handles.input_image, 'Parent', handles.img_in);
set(handles.img_in, 'Visible', 'off');
guidata(handles.figure1, handles);

function util_redraw_output(handles)
oi = zeros(size(handles.input_image));
for i=1:3
    oi(:,:,i) = handles.input_image(:,:,i) .* uint8(handles.output_image);
end
oi = uint8(oi);

imagesc(oi, 'Parent', handles.img_out);
set(handles.img_out, 'Visible', 'off');
guidata(handles.figure1, handles);

function [out] = util_colorize_bw(input)
[rows,cols] = size(input);
out = uint8(zeros(rows, cols, 3));
out(:,:,1) = 255 * input;

function util_threshold(handles)
if(get(handles.pop_version, 'Value') == 1)
    fn = @threshold;
else
    fn = @threshold_student;
end
handles.output_image = logical(fn(handles.input_image, get(handles.thresh_r, 'Value'), ...
                    get(handles.thresh_g, 'Value'), ...
                    get(handles.thresh_b, 'Value')));
util_redraw_output(handles);




% --- Executes just before part1_gui is made visible.
function part1_gui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to part1_gui (see VARARGIN)

% Choose default command line output for part1_gui
handles.output = hObject;

handles.input_image = [];
handles.output_image = [];

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes part1_gui wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = part1_gui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on slider movement.
function thresh_r_Callback(hObject, eventdata, handles)
% hObject    handle to thresh_r (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
set(handles.dthresh_r, 'String', num2str(round(get(hObject, 'Value'))));
util_threshold(handles);


% --- Executes during object creation, after setting all properties.
function thresh_r_CreateFcn(hObject, eventdata, handles)
% hObject    handle to thresh_r (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function thresh_g_Callback(hObject, eventdata, handles)
% hObject    handle to thresh_g (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of
%        slider
set(handles.dthresh_g, 'String', num2str(round(get(hObject, 'Value'))));
util_threshold(handles);


% --- Executes during object creation, after setting all properties.
function thresh_g_CreateFcn(hObject, eventdata, handles)
% hObject    handle to thresh_g (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function thresh_b_Callback(hObject, eventdata, handles)
% hObject    handle to thresh_b (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
set(handles.dthresh_b, 'String', num2str(round(get(hObject, 'Value'))));
util_threshold(handles);

% --- Executes during object creation, after setting all properties.
function thresh_b_CreateFcn(hObject, eventdata, handles)
% hObject    handle to thresh_b (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --------------------------------------------------------------------
function menu_File_Callback(hObject, eventdata, handles)
% hObject    handle to menu_File (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function menu_Image_Callback(hObject, eventdata, handles)
% hObject    handle to menu_Image (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function menu_Im_File_Callback(hObject, eventdata, handles)
% hObject    handle to menu_Im_File (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[file,path] = uigetfile({ '*.bmp;*.jpeg;*.pgm;*.gif;*.png', 'Image Files' }, 'Load Image');
if(file)
    handles.input_image = imread([path file]);
    util_redraw_input(handles);
end


% --------------------------------------------------------------------
function menu_Im_Camera_Callback(hObject, eventdata, handles)
% hObject    handle to menu_Im_Camera (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
xv = videoinput('winvideo');
start(xv);
handles.input_image = getdata(xv, 1);
stop(xv);
util_redraw_input(handles);


% --------------------------------------------------------------------
function menu_Im_Ceiling_Callback(hObject, eventdata, handles)
% hObject    handle to menu_Im_Ceiling (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.input_image = imread(['http://camera1/IMAGE.JPG?cidx=' num2str(now)]);
util_redraw_input(handles);

% --------------------------------------------------------------------
function menu_Im_SaveInput_Callback(hObject, eventdata, handles)
% hObject    handle to menu_Im_SaveInput (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[ file, path ] = uiputfile('*.bmp', 'Save Image');
if(file)
    imwrite(handles.input_image, [path '/' file], 'bmp');
end


% --------------------------------------------------------------------
function menu_Im_SaveOutput_Callback(hObject, eventdata, handles)
% hObject    handle to menu_Im_SaveOutput (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[ file, path ] = uiputfile('*.bmp', 'Save Image');
if(file)
    imwrite(handles.output_image, [path '/' file], 'bmp');
end



% --- Executes on selection change in pop_version.
function pop_version_Callback(hObject, eventdata, handles)
% hObject    handle to pop_version (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns pop_version contents as cell array
%        contents{get(hObject,'Value')} returns selected item from pop_version


% --- Executes during object creation, after setting all properties.
function pop_version_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pop_version (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


