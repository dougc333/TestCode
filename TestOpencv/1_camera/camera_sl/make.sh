#!/bin/bash


g++ camera.cpp -o camera `pkg-config --cflags --libs opencv`

