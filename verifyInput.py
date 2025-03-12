#verifyInput.py

def verifyInteger():       #verifies if the entered value is a valid integer
    lock = True
    
    while lock != False:
        valueRaw = input()
        
        if valueRaw == '':
            print('This field must not be left empty.')
            continue
        else:
            try:
                valueCurated = int(valueRaw)
                lock = False
            except ValueError:
                print('The inputted value is not valid, try again: ')
                continue

    return(valueCurated)

#-------------

def verifyString():     #verifies if the entered value is a string
    lock = True

    while lock != False:
        valueRaw = input()

        if valueRaw == '':
            print('This field must not be left empty.')
            continue
        else:
            try:
                valueCurated = str(valueRaw)
                lock = False
            except ValueError:
                print('The inputted value is not valid, try again: ')
                continue

    return(valueCurated)

#-------------

def verifyFloatingPoint():      #verifies if the enter value is a valid floating-point number
    lock  = True

    while lock != False:
        valueRaw = input()

        if valueRaw == '':
            print('This field must not be left empty.')
            continue
        else:
            try:
                valueCurated = float(valueRaw)
                lock = False
            except ValueError:
                print('The inputted value is not valid, try again: ')
                continue

    return(valueCurated)

#-------------
