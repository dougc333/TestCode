cmake_minimum_required (VERSION 2.8.11)
project (camera_sl)
set (camera_VERSION_MAJOR 1)
set (camera_VERSION_MINOR 0)


add_executable(camera_sl camera.cpp)
include_directories(camera_sl /usr/local/include)
include_directories(camera_sl /usr/local/Cellar/opencv/2.4.13/include)
target_link_libraries(camera_sl /usr/local/lib)
target_link_libraries(camera_sl /usr/local/Cellar/opencv/2.4.13/lib)
