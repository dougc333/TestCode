//
//  main.cpp
//  TestCamera
//
//  Created by Doug Chang on 9/2/16.
//  Copyright © 2016 Doug Chang. All rights reserved.
//

#include <iostream>
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;


int main(int argc, const char * argv[]) {
    cout<<"asdfasdf"<<endl;
    cv::Mat image;
    image = cv::imread("/Users/dc/TestCode/TestMatlab/laneimg1.jpg");
    cv::namedWindow( "Display window", WINDOW_AUTOSIZE ); // Create a window for display.
    cv::imshow( "Display window", image );                // Show our image inside it.
    cv::waitKey(0); // Wait for a keystroke in the window
    return 0;
}
