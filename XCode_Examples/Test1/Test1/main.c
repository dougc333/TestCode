//
//  main.c
//  Test1
//
//  Created by doug chang on 7/26/16.
//  Copyright © 2016 doug chang. All rights reserved.
//

#define _POSIX_C_SOURCE >= 199309L

#include <stdio.h>
#include <time.h>

int main(int argc, const char * argv[]) {
    
    struct timespec start,end;
    
    clock_gettime(CLOCK_MONOTONIC,&start);
    printf("Hello, World!\n");
    return 0;
}


