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

safe_points = []
noofbacteria = 0;
bacteria = []

def main_logic():
    is_safe = []
    print ('Main Logic')
    for indibacteria in bacteria:
        print ('Processing ' + str(indibacteria[0]) + ", " + str(indibacteria[1]) )
        
    print (is_safe)


def inp():
    roomsizex = int(input('Enter X dimension of Room'))
    roomsizey = int(input('Enter Y dimension of Room'))
    bulb_x = int(input('Enter X dimension of Bulb'))
    bulb_y = int(input('Enter Y dimension of Bulb'))
    noofbacteria = int(input('Enter number of bacteria'))
    samplex = 0
    sampley = 0
    for i in range(noofbacteria):
        print('Enter value of ' + str(i) + " bacteria")
        samplex = int(input('Enter x dimension of bacteria '))
        sampley = int(input('Enter x dimension of bacteria '))
        bacteria.append((samplex, sampley))
    print(bacteria)
    main_logic()

        


inp()
# def same_line():
#     virus = [(1,2), ()]