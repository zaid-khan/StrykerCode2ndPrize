bulb_x_parity = 0
bulb_y_parity = 0


#Input code here

    
def verticaltest(bacteria_x_parity, bacteria_y_parity):
    if bulb_x == bacteria_x_parity or bulb_y == bacteria_y_parity:
        return True
    

def invalidin(bac_x, bac_y):
    if bac_x < 0 or bac_x > sizex:
        return True
    elif bac_y < 0 or bac_y > sizey:
        return True
    return False

#store bacteria position in tuples
def calling_logic():
    output = ""

    for virus in listofbacteria:
        # print(virus[0])
        bacteria_x_parity = int(virus[0]) % 2
        bacteria_y_parity = int(virus[1]) % 2
        
        if invalidin(int(virus[0]), int(virus[1])):
            output += '0 '
            continue

        if verticaltest(int(virus[0]), int(virus[1])):
            output += '1 '
            continue
        
        if bulb_x_parity == bacteria_x_parity:
            if bulb_y_parity != bacteria_y_parity:
                output += '0 '
            else:
                output += '1 '
        else:
            if bulb_y_parity != bacteria_y_parity:
                output += '1 '
            else:
                output += '0 '
        

    print (output)


sizex = list(map(int,input().split()))
sizey = list(map(int,input().split()))
bulbcordinate = list(map(int,input().split()))
noofbacteria = list(map(int,input().split()))

noofbacteria = int(noofbacteria[0])
sizex = int(sizex[0])
sizey = int(sizey[0])
bulb_x = int(bulbcordinate[0])
bulb_y = int(bulbcordinate[1])


listofbacteria = []
for i in range(noofbacteria):
    listofbacteria.append(list(map(int,input().split())))

bulb_x_parity = bulb_x % 2
bulb_y_parity = bulb_y % 2

calling_logic()
