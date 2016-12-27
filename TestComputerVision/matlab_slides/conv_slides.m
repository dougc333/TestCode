img = fopen('/Users/dougchang/TestCode/TestMatlab/week10')

x=[1 2 3; 4 5 6; 7 8 9]
h=[-1 -2 -1; 0 0 0; 1 2 1]

conv=conv2(x,h,'same')
