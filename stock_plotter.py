
###
### Author: Xin Li
### Description: stock_plotter.py
###This program works by accepting 2 values.
###The first value is a string, specifying the
###mode to run in. The first input should be
###one of two strings: vertical or horizontal,
###which should control the orientation of the plot.
###The second input should be a string, which will
###specify the way the plot should be drawn. This
###will be covered more in a later section of this spec.
###

mode = input('Enter stock plotter mode:\n')
while mode != 'horizontal' and mode != 'vertical':
    print('what?')
    mode = input('Enter stock plotter mode:\n')

string = input('Enter stock plot input string:\n')
while len(string) %2 != 0 :
    string = input('Enter stock plot input string:\n')

    #y-x graph
if mode == 'vertical':
    #vertical
    print('#'*19)
    x = (len(string)) / 2
    i = 0
    x = 8
    while i < len(string) :
        move = string[i]
        move_x = string[i+1]
        if move == 'u':
            x += int(move_x)
        if move == 'd':
            x -= int(move_x)
        i += 2
        print('#',' '*x,'*',' '*(16-x),'#',sep='')
    print('#'*19)
    exit(0)

if mode == 'horizontal':
    #horizontal
    double_x = float(len(string))
    x = double_x / 2
    x = int(x)
    x = x + 2
    print('#' * (x+2))
    i = 0
    index = 0
    y = 8
    y = int(y)
    point_x0 = 0
    x_total = 0
    while i < 17 :
        index = 0
        num = 0
        print('# ',end='')
        while index < len(string) :
            point_x = (index+2)/2
            point_x = int(point_x)
            deta_x = point_x - point_x0
            point_x0 = point_x
            index = int(index)
            move = string[index]
            move_y = string[index+1]
            if move == 'u':
                y -= int(move_y)
            if move == 'd':
                y += int(move_y)
            if y==i:
                print(' '*(deta_x-1),'*',sep='',end='')
                num += 1
            if y!=i:
                print(' '*(deta_x-1),' ',sep='',end='')
            x_total += deta_x
            index += 2
        print(' '*(x-1-x_total),'#',sep='')
        y=8
        i += 1
    print('#' * (x+2))
