#inputControl.py

def verifyInteger():       #verifies if the given value is an integer
    lock = True
    
    while lock != False:
        valueRaw = input()
        
        if valueRaw = '':
            print('This field must not be left empty.')
            continue
        else:
            try:
                valueCurated = int(valueRaw)
                lock = False
            except ValueError:
                print('The inputted value is not valid, try again: )
                continue

    return(valueCurated)
