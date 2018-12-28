'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

#Upper limit of x and y or room size
roomsizex = 3
roomsizey = 4

#Location of the bulb
bulb_x = 1
bulb_y = 2

#
points = ()

verticaltest = []
horitest = []
diagtest = []

def vertical_line():
    #x = 
    x = bulb_x
    y = bulb_y
    
    temp_point = ()
    while y < roomsizey:
        temp_point = (x, y+1)
        verticaltest.append(temp_point)
        y += 1
    
    y = bulb_y
    while y > 0:
        temp_point = (x, y-1)
        verticaltest.append(temp_point)
        y -= 1

    print(verticaltest)


def horizontal_line():
    #x = 
    x = bulb_x
    y = bulb_y
    
    temp_point = ()
    while x < roomsizex:
        temp_point = (x+1, y)
        horitest.append(temp_point)
        x += 1
    
    x = bulb_x

    while x > 0:
        temp_point = (x-1, y)
        horitest.append(temp_point)
        x -= 1

    print(horitest)


def edge_reached(x, y):

    if ((x == 0) or (x == bulb_x)):
        return 1
    
    elif ((y == 0) or (y == bulb_y)):
        return 0

def corner_reached(x, y):
    
    if (x == 0) and (y == 0):
        return 1
    elif (x == 0) and (y == roomsizey):
        return 1
    elif (y == 0) and (x == roomsizex):
        return 1
    elif (x == roomsizex) and (y == roomsizey):
        return 1



def top_left(x, y):
    if (corner_reached(x, y) == 1):
        return

    if (y == roomsizey) or (x == 0):
        return

    temp_point = ()

    x = bulb_x
    y = bulb_y
    xinc = -1
    yinc = 1

    while (True):
        x += xinc
        y += yinc
        temp_point = (x, y)
        print(temp_point)
        diagtest.append(temp_point)
        
        if (edge_reached(x, y) == 1):
            xinc *= -1
        elif (edge_reached(x, y) == 0):
            yinc *= -1

            
        if corner_reached(x,y):
            break



def diag_line():
    x = bulb_x
    y = bulb_y
    top_left(x, y)
    
    print(diagtest)

    
    
    # parity = edge_reached(x, y)
    # print (parity)




diag_line()


# vertical_line()
# horizontal_line()

